# -*- coding: utf-8 -*-
from gluon import *

def single_table_spe_grid(table, fields=None,add=True,view=True,edit=True,delete=True):
    sqlform_grid = SQLFORM.grid(table,
                                fields=fields,
                                deletable=delete,
                                editable=edit,
                                details=view,
                                create=add,
                                csv=False,
                                maxtextlength=40,
                                showbuttontext=False,
                                )
    return sqlform_grid