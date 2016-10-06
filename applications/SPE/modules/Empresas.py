#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Empresa(Model):
    #Building database object
    def __init__(self):
    	super(Empresa,self).__init__(tableName="Empresa")