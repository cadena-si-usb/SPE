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
	#Building database object
	def __init__(self):
		super(Usuario,self).__init__(tableName="UsuarioUSB")

	def getByRole(self,id):
		usuario = None

		row = self.db((self.table.id == id) & (self.db.auth_membership.user_id==self.table.id)
					  & (self.db.auth_group.id == self.db.auth_membership.group_id)).select().first()
		usuarioUSB = row.UsuarioUSB
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

				current.auth.add_membership(user_id=usuarioUSB["id"],role=rol["role"])
			 
        	return usuarioUSB


	def registrar(self,usuario,auth):
		rol = obtenerRoles(self.db,usuario['tipo'])

		nombre = usuario['first_name']
		apellido = usuario['last_name']
		tipo = usuario['tipo']
		carnet = usuario['email'].split('@')[0]
		clave = random_key()

		try:
			auth_User_Id=self.db.auth_user.insert(first_name=nombre,
									 last_name=apellido,
									 username=carnet,
									 password=self.db.auth_user.password.validate(clave)[0])
			usuario = self.table.insert(id=auth_User_Id,
										auth_User=auth_User_Id,
										nombre=nombre,
										apellido=apellido,
										usbid=carnet,
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
			elif (tipo == 'Profesor'):
				auth.add_membership(role='Profesor', user_id=auth_User_Id)
			elif (tipo == 'Coordinador'):
				auth.add_membership(role='Coordinador', user_id=auth_User_Id)

			auth.login_bare(carnet,clave)
			return auth_User_Id

		except Exception as e:
			print 'ERROR: ',
			print e

