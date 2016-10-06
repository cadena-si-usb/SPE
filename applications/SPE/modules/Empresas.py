#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Ejecucion(Model):
    #Building database object
    def __init__(self):
    	super(Ejecucion,self).__init__(tableName="Ejecucion")