#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Inscripcion(Model):
    #Building database object
    def __init__(self):
    	super(Inscripcion,self).__init__(tableName="Inscripcion")