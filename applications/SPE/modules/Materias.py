#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Materia(Model):
    #Building database object
    def __init__(self):
    	super(Materia,self).__init__(tableName="Materia")