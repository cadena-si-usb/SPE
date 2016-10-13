#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Area_Proyecto(Model):
    #Building database object
    def __init__(self):
        super(Area_Proyecto,self).__init__(tableName="Area_Proyecto")