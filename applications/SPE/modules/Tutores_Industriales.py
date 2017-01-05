#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Tutor_Industrial(Model):
    #Building database object
    def __init__(self):
    	super(Tutor_Industrial,self).__init__(tableName="Tutor_Industrial")