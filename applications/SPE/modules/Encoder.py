#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *

def to_dict(storage):
    obj = {}
    for attr in storage:
        obj[attr] = storage[attr]

    return obj

def enQuery(self,where):
    first = True
    condition = ""

    if where != "self.table":
        for cond in where:
            if first:
                first = False
                condition = eval(cond)
            else:
                condition &= eval(cond)
    else:
        condition = eval(where)

    return condition
