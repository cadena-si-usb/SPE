#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Colocacion(Model):
    #Building database object
    def __init__(self):
    	super(Colocacion,self).__init__(tableName="Colocacion")