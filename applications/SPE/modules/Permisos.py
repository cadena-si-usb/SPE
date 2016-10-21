#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
import ast
from APIhandler import Model
import Encoder

class Permiso(Model):
    #Building database object
    def __init__(self):
    	super(Permiso,self).__init__(tableName="Permiso")


class Permiso_Evaluacion(Model):
    #Building database object
    def __init__(self):
    	super(Permiso_Evaluacion,self).__init__(tableName="Permiso_Evaluacion")

