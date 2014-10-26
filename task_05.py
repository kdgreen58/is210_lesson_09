#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_05 Assignment 9"""

from functools import reduce
import operator


def mass_multiplier(*args):
    """ Accepts any number of positional arguments
        returns multiplication result of all arguments

        Args:
        *args: arbitrary list of numbers of
            any type
        Return:
        Number as the multiplication result of all arguments

        Example:
        >>> mass_multiplier(22, 34, 10, 5)
        >>> 37400
        >>> mass_multiplier(3.45, 4.98, 1.76)
        >>> 30.23856
    """
    multiplied = reduce(operator.mul,(args),1)
    return multiplied


def student_report(name, age, school_id, **kwargs):
    """Returns student report

    Args:
    name(str): student name as string
    age (int): student age as number
    school_id(str): ID of student school
    *kwargs: any additional key word arguments

    Reurns:
    dictionary

    Examples:
    >>> student_report(name='Jane', age=13, school_id='ps-1')
    >>> {'name': 'Jane', 'age': 3, 'school_id': 'ps-1')

    >>> student_report(name='Jane', age=13, school_id='ps-1', math='B')
    >>> {'name': 'Jane', 'age': 3, 'school_id': 'ps-1', 'math'=B)

    """
    returndict = dict(name = name, age = age, school_id = school_id, **kwargs)
    return returndict
