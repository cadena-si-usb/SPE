#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Rol(Model):
    #Building database object
    def __init__(self):
    	super(Rol,self).__init__(tableName="auth_group")