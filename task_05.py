#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_05 Assignment 9"""

from functools import reduce
import operator

def mass_multiplier(*args):
    multiplied = reduce(operator.mul,(args),1)
    return multiplied

def student_report(name, age, school_id, **kwargs):
    returndict = dict(name = name, age = age, school_id = school_id, **kwargs)
    return returndict
