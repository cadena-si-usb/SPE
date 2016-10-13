#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Dedicacion(Model):
    #Building database object
    def __init__(self):
    	super(Dedicacion,self).__init__(tableName="Dedicacion")