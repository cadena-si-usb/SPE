#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Area_Laboral(Model):
    #Building database object
    def __init__(self):
        super(Area_Laboral,self).__init__(tableName="Area_Laboral")