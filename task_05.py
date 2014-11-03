#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 Code"""


def mass_multiplier(*args):
    """Docstirng



    """
    retval = 1
    for arg in args:
        retval *= arg
    return retval

def student_report(name, age, school_id, **kwargs):
    """Docstring


    """
    kwargs['name'] = name
    kwargs['age'] = age
    kwargs['school_id'] = school_id
    return kwargs
