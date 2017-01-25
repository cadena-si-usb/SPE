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
    def reprobar(self,id):
        plan_de_trabajo = self.db(self.table.id == id).select().first()
        # Verificamos si hay que revertir aprobaciones para evitar ir a la base de datos innecesariamente
        if (plan_de_trabajo.aprobacion_tutor_academico != "En Espera"
             or plan_de_trabajo.aprobacion_tutor_industrial != "En Espera"
             or plan_de_trabajo.aprobacion_coordinacion != "En Espera"
             or plan_de_trabajo.estado != "Sin Enviar"):
            # Cambiamos el estado
            plan_de_trabajo.update_record(
                aprobacion_tutor_academico="En Espera",
                aprobacion_tutor_industrial="En Espera",
                aprobacion_coordinacion="En Espera",
                estado="Sin Enviar")

    # Funcion que retorna True si el plan fue enviado y aprobado,False de lo contrario
    @staticmethod
    def comprobarPlanAprobado(db,planId):
        plan_trabajo = db.Plan_Trabajo(id=planId)
        # Verificamos si hay que revertir aprobaciones para evitar ir a la base de datos innecesariamente
        if (plan_trabajo.aprobacion_tutor_academico=="Aprobado"
            and plan_trabajo.aprobacion_tutor_industrial=="Aprobado"
            and plan_trabajo.aprobacion_coordinacion=="Aprobado"
            and plan_trabajo.estado=="Enviado"):
            return True
        else:
            return False

    # Funcion que retorna True si el plan fue enviado y aprobado,False de lo contrario
    @staticmethod
    def esActorDePlan(db,userId,id):
        pasantia = db.Pasantia(id=id)
        estudiante = db.Estudiante(id=pasantia.estudiante)
        tutor_academico = db.Estudiante(id=pasantia.tutor_academico)
        tutor_industrial = db.Tutor_Industrial(id=pasantia.tutor_industrial)
        # Verificamos si hay que revertir aprobaciones para evitar ir a la base de datos innecesariamente
        try:
            resultado=(tutor_industrial.usuario==userId
                       or estudiante.usuario==userId
                       or tutor_academico.usuario==userId)
            if not resultado:
                coordID=db((db.Coordinador.usuario==userId) & (db.Coordinador.coordinacion==pasantia.estudiante.carrera.coordinacion))
                if coordID:
                    return True
                else:
                    return False
            return resultado
        except:
            return False