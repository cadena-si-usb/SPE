#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
import APIhandler
from APIhandler import Model
import Encoder
from ast import literal_eval as to_object

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
		super(Usuario,self).__init__(tableName="UsuarioExterno")

	def getByRole(self,id):
		usuario = None
		usuario = self.db((self.table.id==id) & (self.db.auth_user.id==self.table.auth_User)
						  & (self.db.Empresa.usuario==self.table.id
							 or self.db.Tutor_Industrial.usuario==self.table.id)).select().first()

		return usuario
