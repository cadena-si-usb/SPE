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
    def reprobar(self):
        # Verificamos si hay que revertir aprobaciones para evitar ir a la base de datos innecesariamente
        if ((self.aprobacion_tutor_academico != "En Espera"
             or self.aprobacion_tutor_industrial != "En Espera"
             or self.aprobacion_coordinacion != "En Espera")
            and self.estado != "Enviado"):
            # Cambiamos el estado
            self.update_record(
                aprobacion_tutor_academico="En Espera",
                aprobacion_tutor_industrial="En Espera",
                aprobacion_coordinacion="En Espera",
                estado="Sin Enviar")