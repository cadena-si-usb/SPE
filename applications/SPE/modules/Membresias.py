#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Membresia(Model):
    #Building database object
    def __init__(self):
    	super(Membresia,self).__init__(tableName="auth_membership")