#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Acceso_Etapa(Model):
    #Building database object
    def __init__(self):
    	super(Acceso_Etapa,self).__init__(tableName="Acceso_Etapa")

    def full(self,rol):
    	rows = self.db((self.table.rol == rol) & (self.table.etapa == self.db.Etapa.id)).select()

    	return rows
