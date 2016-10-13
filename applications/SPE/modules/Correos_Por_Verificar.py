#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Correo_Por_Verificar(Model):
    #Building database object
    def __init__(self):
    	super(Correo_Por_Verificar,self).__init__(tableName="correo_por_verificar")