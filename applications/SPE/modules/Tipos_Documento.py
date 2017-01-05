#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Tipo_Documento(Model):
    #Building database object
    def __init__(self):
    	super(Tipo_Documento,self).__init__(tableName="Tipo_Documento")