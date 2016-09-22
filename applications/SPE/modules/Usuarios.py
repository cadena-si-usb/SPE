#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder
from ast import literal_eval as to_object
from usbutils import random_key

def obtenerRoles(db,tipo):
	if (tipo == 'Pregrado'):
		rol = db(db.Rol.nombre == 'Estudiante').select().first().as_dict()
		rol = rol['id']
	else:
		rol = db(db.Rol.nombre == 'Invitado').select().first().as_dict()
		rol = rol['id']

	return str(rol)

class Usuario(Model):
	#Building database object
	def __init__(self):
		super(Usuario,self).__init__(tableName="UsuarioUSB")

	def getByRole(self,id):
		usuario = None

		row = self.db((self.table.usbid == id) & (self.table.rol == self.db.Rol.id)).select().first()

		if (row != None):
			usuario = {}
			rol = row.Rol
			usuarioUSB = row.UsuarioUSB

			if (not rol):
				if (rol["nombre"] == "CoordinadorCCT"):
					usuario = self.db(self.db.Coordinador.usuario == usuarioUSB["id"]).select().first()
				elif (rol["nombre"] == "AdministrativoCCT"):
					usuario = self.db(self.db.Administrativo.usuario == usuarioUSB["id"]).select().first()
				elif (rol["nombre"] == "CoordinadorCarrera"):
					usuario = self.db(self.db.Coordinador.usuario == usuarioUSB["id"]).select().first()
				elif (rol["nombre"] == "Estudiante"):
					usuario = self.db(self.db.Estudiante.usuario == usuarioUSB["id"]).select().first()
				elif (rol["nombre"] == "Profesor"):
					usuario = self.db(self.db.Profesor.usuario == usuarioUSB["id"]).select().first()

			usuarioUSB["rol"] = rol["id"]
			#auth.add_membership(usuarioUSB["id"],rol["id"])
			 
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
			usuario = self.table.insert(auth_User=auth_User_Id,
										nombre=nombre,
										apellido=apellido,
										usbid=carnet,
										rol=rol,
										clave=clave,
										activo=False)

			if (tipo == 'Pregrado' or tipo == 'Postgrado'):
				estudiante = self.db.Estudiante.insert(usuario=usuario['id'],
										carnet=carnet,
										activo=False)
				self.db.Curriculo.insert(estudiante=estudiante['id'],
										activo=False)
				group_id = auth.id_group(role='Estudiante')
				auth.add_membership(group_id, auth_User_Id)
			elif (tipo == 'Profesor'):
				group_id = auth.id_group(role='Profesor')
				auth.add_membership(group_id, auth_User_Id)
			elif (tipo == 'Coordinador'):
				group_id = auth.id_group(role='Coordinador')
				auth.add_membership(group_id, auth_User_Id)

			auth.login_bare(carnet,clave)

		except Exception as e:
			print 'ERROR: ',
			print e

