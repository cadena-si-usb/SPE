#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
import ast
from APIhandler import Model
import Encoder

class Pasantia(Model):
    #Building database object
    def __init__(self):
    	super(Pasantia,self).__init__(tableName="Pasantia")

    def JMaterias(self, options):
        filter = ast.literal_eval(options['filter'])

        rows = self.db((self.table.materia == self.db.Materia.id) & (self.table.periodo == self.db.Periodo.id) & (self.table.estudiante == filter['estudiante'])).select()

        return rows
