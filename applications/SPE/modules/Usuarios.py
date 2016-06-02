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

    	row = self.db((self.table.usbid == id) & (self.table.rol == self.db.Rol.id)).select()[0]

    	rol = row.Rol
    	usuarioUSB = row.UsuarioUSB

    	if (rol):
	    	if (rol["nombre"] == "CCT"):
	    		usuario = self.db(self.db.Coordinador.usuario == usuarioUSB["id"]).select()[0].as_dict()
	    	elif (rol["nombre"] == "Estudiante"):
	    		usuario = self.db(self.db.Estudiante.usuario == usuarioUSB["id"]).select()[0].as_dict()

	    	usuario["rol"] = rol["id"]

    	return usuario
		 

