#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Plan_Trabajo(Model):
    #Building database object
    def __init__(self):
    	super(Plan_Trabajo,self).__init__(tableName="Plan_Trabajo")