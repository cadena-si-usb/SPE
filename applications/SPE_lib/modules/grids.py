# -*- coding: utf-8 -*-
from gluon import *


def simple_spe_grid(
        table, fields=None, add=True, view=True, edit=True, delete=True,
        field_id=None,orderby=None,searchable=True, links=None):
    sqlform_grid = SQLFORM.grid(table,
                                fields=fields,
                                deletable=delete,
                                editable=edit,
                                details=view,
                                create=add,
                                csv=False,
                                maxtextlength=40,
                                showbuttontext=False,
                                field_id=field_id,
                                orderby=orderby,
                                searchable=searchable,
                                links=links,
                                )
    return sqlform_grid
