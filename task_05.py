#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mass_multiplier(*args):
    total = 1
    for i in args:
        total *= i
    return total

def student_report(name, age, school_id, **kwargs):
    for k, v in kwargs.iteritems():
        stuff ={'name': name,
                'age': age,
                'school_id': school_id,
                k: v
                }
        return stuff
