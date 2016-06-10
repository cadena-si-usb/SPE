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

			if (rol != None):
				if (rol["nombre"] == "CCT"):
					usuario = self.db(self.db.Coordinador.usuario == usuarioUSB["id"]).select().first()
				elif (rol["nombre"] == "Estudiante"):
					usuario = self.db(self.db.Estudiante.usuario == usuarioUSB["id"]).select().first()

				usuarioUSB["rol"] = rol["id"]

		return usuarioUSB


	def registrar(self,usuario,auth):
		rol = obtenerRoles(self.db,usuario['tipo'])

		nombre = usuario['first_name']
		apellido = usuario['last_name']
		tipo = usuario['tipo']
		carnet = usuario['email'].split('@')[0]
		clave = random_key()

		try:
			usuario = self.table.insert(nombre=nombre,
									apellido=apellido,
									usbid=carnet,
									rol=rol,
									clave=clave,
									activo=False)
			self.db.auth_user.insert(first_name=nombre,
									 last_name=apellido,
									 username=carnet,
									 password=self.db.auth_user.password.validate(clave)[0])

			if (tipo == 'Pregrado'):
				estudiante = self.db.Estudiante.insert(usuario=usuario['id'],
										carnet=carnet,
										activo=False)
				self.db.Curriculo.insert(estudiante=estudiante['id'],
										activo=False)

			auth.login_bare(carnet,clave)

		except Exception as e:
			print 'ERROR: ',
			print e

