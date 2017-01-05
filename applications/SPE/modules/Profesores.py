#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Profesor(Model):
    #Building database object
    def __init__(self):
    	super(Profesor,self).__init__(tableName="Profesor")