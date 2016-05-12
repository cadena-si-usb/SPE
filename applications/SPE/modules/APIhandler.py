#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
import Encoder

class Model(object):
    #Building database object
    def __init__(self, tableName=None):
        self.db = current.db
        self.tableName = tableName
        self.session = current.session
        self.request = current.request
        self.response = current.response
        self.cache = current.cache
        self.table = getattr(self.db,tableName)

    def form(self,projection):
        return SQLFORM(self.table,fields=projection)

    def find(self,options):
        query = DBhandler.getQuery(options)

        condition = query['condition']
        order = query['order']
        limit = query['limit']

        where = Encoder.enQuery(self,condition)
        rows = self.db(where).select(orderby=eval(order),limitby=limit)

        return rows

    def count(self,options):
        query = DBhandler.getQuery(options)

        condition = query["condition"]

        where = Encoder.enQuery(self,condition)

        return self.db(where).count()

    #TODO
    def create(self,item):
        return "SOON"

    #TODO
    def update(self,id,changes):
        return "SOON"

    #TODO
    def delete(self,id):
        return "SOON"

    #TODO
    def show(self,id):
        return "SOON"
