#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import ast

#PRIVATE FUNCTIONS
def _limitQuery(options):
    if not "limit" in options:
        limit = "4"
    else:
        limit = options["limit"]

    if not "page" in options:
        starts = "0"
    else:
        starts = options["page"]

    return (int(starts),int(starts) + int(limit))

def _orderQuery(options):
    if not "order" in options:
        order = "id"
    else:
        order = options["order"]

    if not "side" in options:
        side = ">"
    else:
        side = options["side"]

    query = ""
    if side == "<":
        query += "~"

    return query + "self.table." + order

def _filterQuery(filter):
    filters = ast.literal_eval(filter)

    filterQuery = ""
    first = True

    for attr in filters:
        if first:
            first = False
        else:
            filterQuery += " and "

        filterQuery += "self.table." + attr + " == '" + filters[attr] + "'"

    return filterQuery

def _searchTerm(term):
    search = ast.literal_eval(term)
    return "self.table." + search["key"] + ".startswith('" + search["value"] + "')"

def _conditionalQuery(options):
    conditions = []

    if "filter" in options and options["filter"] != "{}":
        conditions.append(_filterQuery(options["filter"]))

    if "searchTerm" in options and options["searchTerm"] != "{}":
        conditions.append(_searchTerm(options["searchTerm"]))

    if len(conditions) == 0:
        return "self.table"

    return conditions

def getQuery(options):
    orderBy = _orderQuery(options)
    limitBy = _limitQuery(options)
    condition = _conditionalQuery(options)

    return {'order':orderBy, 'limit': limitBy, 'condition': condition}
