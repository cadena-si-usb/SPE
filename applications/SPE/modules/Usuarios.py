#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder
from ast import literal_eval as to_object
from usbutils import random_key
from gluon import current

def obtenerRoles(db,tipo):
	if (tipo == 'Pregrado'):
		rol = db(db.auth_group.role=='Estudiante').select().first().as_dict()
		rol = rol['id']
	else:
		rol = db(db.auth_group.role == 'Invitado').select().first().as_dict()
		rol = rol['id']

	return str(rol)

class Usuario(Model):
	'''

	'''
	#Building database object
	def __init__(self):
		super(Usuario,self).__init__(tableName="auth_user")

	def getByRole(self,id):
		'''

		:param id:
		:return:
		'''
		usuario = None

		row = self.db((self.table.id == id) & (self.db.auth_membership.user_id==self.table.id)
					  & (self.db.auth_group.id == self.db.auth_membership.group_id)).select().first()
		usuarioUSB = row.auth_user
		rol = row.auth_group
		if (row != None):
			usuario = {}

			if (not rol):
				if (rol["role"] == "CoordinadorCCT"):
					usuario = self.db(self.db.Coordinador.usuario == usuarioUSB["id"]).select().first()
				elif (rol["role"] == "AdministrativoCCT"):
					usuario = self.db(self.db.Administrativo.usuario == usuarioUSB["id"]).select().first()
				elif (rol["role"] == "Coordinador"):
					usuario = self.db(self.db.Coordinador.usuario == usuarioUSB["id"]).select().first()
				elif (rol["role"] == "Estudiante"):
					usuario = self.db(self.db.Estudiante.usuario == usuarioUSB["id"]).select().first()
				elif (rol["role"] == "Profesor"):
					usuario = self.db(self.db.Profesor.usuario == usuarioUSB["id"]).select().first()
				elif (rol["role"] == "Administrativo"):
					usuario = self.db(self.db.Administrativo.usuario == usuarioUSB["id"]).select().first()

				current.auth.add_membership(user_id=usuarioUSB["id"],role=rol["role"])
			 
        	return usuarioUSB


	def registrar(self,usuario,auth):
		'''
		Crea un usuario a partir de datos del CAS

		:param usuario: Datos de usuario retornados por el CAS
		:param auth: Modulo de Auth usado por la aplicacion
		:return: Id del usuario en la tabla de auth_user
		'''
		rol = obtenerRoles(self.db,usuario['tipo'])

		first_name = usuario['first_name']
		last_name = usuario['last_name']
		tipo = usuario['tipo']
		carnet = usuario['email'].split('@')[0]
		clave = random_key()

		try:
			auth_User_Id=self.db.auth_user.insert(first_name=first_name,
									 last_name=last_name,
									 username=carnet,
									 password=self.db.auth_user.password.validate(clave)[0])
			usuario = self.table.insert(id=auth_User_Id,
										auth_User=auth_User_Id,
										first_name=first_name,
										last_name=last_name,
										username=carnet,
										clave=clave,
										activo=False)

			if (tipo == 'Pregrado' or tipo == 'Postgrado'):
				estudiante = self.db.Estudiante.insert(
					id=auth_User_Id,
					usuario=usuario['id'],
					carnet=carnet,
					activo=False)
				self.db.Curriculo.insert(estudiante=estudiante['id'],
										activo=False)
				auth.add_membership(role='Estudiante', user_id=auth_User_Id)
			elif (tipo == 'Docente'):
				profesor = self.db.Profesor.insert(
					id=auth_User_Id,
					usuario=usuario['id'],
					activo=False)
				auth.add_membership(role='Profesor', user_id=auth_User_Id)
			elif (tipo == 'Coordinador'):
				coordinador = self.db.Coordinador.insert(
					id=auth_User_Id,
					usuario=usuario['id'],
					carnet=carnet,
					activo=False)
				auth.add_membership(role='Coordinador', user_id=auth_User_Id)
			elif (tipo == 'Administrativo'):
				administrativo = self.db.Administrativo.insert(
					id=auth_User_Id,
					usuario=usuario['id'],
					carnet=carnet,
					activo=False)
				auth.add_membership(role='Administrativo', user_id=auth_User_Id)
			else:
				auth.add_membership(role='Invitado', user_id=auth_User_Id)
			# Como el usuario ya esta registrado, buscamos sus datos y lo logueamos.
			datosAuth = self.db(self.db.auth_user.id == auth_User_Id).select().first()
			# Iniciamos Sesion
			auth.user = datosAuth
			auth.login_user(datosAuth)
			return auth_User_Id

		except Exception as e:
			print 'ERROR: ',
			print e

	def getUserActions(self,context=None):
		'''
		Retorna la lista de las URL's sobre las cuales tiene permiso el usuario en sesion

		:param context: Filtro opcional para las acciones bajo un context especifico
		:return: String[]
		'''
		roles = current.auth.user_groups
		acciones = None
		for rol in roles:
			if context:
				if acciones:
					acciones.records.append(self.db((self.db.Accion_Usuario.rol == rol) & (self.db.Accion_Usuario.contexto == context)).select(
						self.db.Accion_Usuario.destino,orderby=self.db.Accion_Usuario.first_name))
				else:
					acciones=(self.db(
						(self.db.Accion_Usuario.rol == rol) & (self.db.Accion_Usuario.contexto == context)).select(
						self.db.Accion_Usuario.destino,orderby=self.db.Accion_Usuario.first_name))
			else:
				if acciones:
					acciones.records.append(
						self.db((self.db.Accion_Usuario.rol == rol)).select(
							self.db.Accion_Usuario.destino,orderby=self.db.Accion_Usuario.first_name))
				else:
					acciones= self.db((self.db.Accion_Usuario.rol == rol)).select(
						self.db.Accion_Usuario.destino,orderby=self.db.Accion_Usuario.first_name)
		destinos=[]
		for accion in acciones:
			destinos.append(accion.destino)
		return destinos

	def checkUserPermission(self,action):
		'''
		Busca si alguno de los roles del usuario logeado tiene permiso sobre el url deseado

		:param action: URL a la que se quiere acceder
		:return: True si se cumple el requerimiento
		'''
		if not current.auth.is_logged_in():
			redirect(URL(c='default', f='index'))
		acciones = self.getUserActions()
		if action in acciones:
			return True
		else:
			redirect(URL(c='default',f='index'))
		return (action in acciones)