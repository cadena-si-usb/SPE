#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

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
		    		usuario = self.db(self.db.Coordinador.usuario == usuarioUSB["id"]).select().as_dict()
		    	elif (rol["nombre"] == "Estudiante"):
		    		usuario = self.db(self.db.Estudiante.usuario == usuarioUSB["id"]).select().as_dict()

		    	usuario["rol"] = rol["id"]

    	return usuario
		 

