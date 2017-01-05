#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Accion_Usuario(Model):
    #Building database object
    def __init__(self):
    	super(Accion_Usuario,self).__init__(tableName="Accion_Usuario")

def construirAccion(application,controller):
    return '/'+application+'/'+controller+'/'+'listar'