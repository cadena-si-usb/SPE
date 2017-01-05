#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Division(Model):
    #Building database object
    def __init__(self):
    	super(Division,self).__init__(tableName="Division")