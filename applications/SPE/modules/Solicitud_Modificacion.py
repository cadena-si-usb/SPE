#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Solicitud_Modificacion(Model):
    #Building database object
    def __init__(self):
    	super(Solicitud_Modificacion,self).__init__(tableName="Solicitud_Modificacion")
