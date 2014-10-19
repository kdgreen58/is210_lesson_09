==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #08
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-10-14T09:00:00-0400
:Due-Date: 2014-10-20T09:00:00-0400

Overview
========

The following tasks will either have you interacting with existing files in
the starter repo or creating new ones on the fly. Don't forget to add your
interpreter directive, utf-8 encoding, and a short docstring with any new files
that you create!

Task 01: Create a Package
=========================

We'll assume you're comfortable with basic module creation and will move
straight on to package creation.

Specifications
^^^^^^^^^^^^^^

#.  Create a package called ``task_01``

#.  Create a module in ``task_01`` named ``peanut``

#.  In ``peanut``, create a constant named ``BUTTER`` and have it return a
    truthy value.

#.  In ``peanut``, create a second constant named ``OIL`` and assign it a
    falsy value

Task 02: Import a Module Namespace
==================================

We'll begin our importation practice by importing a module with its full
namespace. Generally, this is the safest way to import modules though it's not
always the most practical.

Specifications
^^^^^^^^^^^^^^

#.  Create a module called ``task_02``

#.  Import the ``peanut`` module from the ``task_01`` package

#.  Create a new constant in ``task_02`` called, ``TIME`` and assign it the
    value from ``BUTTER`` constant of the ``peanut`` module

Task 03: Copy a Module Attribute
================================

Our next import adventure has us copying module attributes into the current
namespace.

Specifications
^^^^^^^^^^^^^^

#.  Create a module called ``task_03``

#.  Copy the ``BUTTER`` constant from the ``peanut`` module into the ``task_03``
    namespace

#.  Create a new constant called ``JELLY`` and assign its value from the
    copied ``BUTTER`` attribute

Task 04: The __main__ Scope
===========================

We'll use the ``__main__`` to set up conditional execution for a module.

Specifications
^^^^^^^^^^^^^^

#.  Create a module named ``task_04``

#.  Create a constant named ``RAN`` and assign it a value of ``False``

#.  Use the ``__main__`` scope to change the value of ``RAN`` to ``True`` when
    ``task_04`` is run on the command line

Examples
^^^^^^^^

.. code:: console

    $ python -i task_04.py
    >>> RAN
    True

.. code:: pycon

    >>> import task_04
    >>> task_04.RAN
    False

.. warning::

    This task does not have 100% unit test coverage. You will have to get the
    scope portion correct on your own.

Task 05: \*args and \*\*kwargs
==============================

Finally, for this lesson, we'll be using the magic arguments in a function.

Specifications
^^^^^^^^^^^^^^

#.  Create a module named ``task_05``

#.  In ``task_05``, create a function named ``mass_multiplier()``

    #.  ``mass_multiplier()`` should accept any number of positional (indexed)
        arguments

    #.  It returns the multiplication result of all arguments

#.  In ``task_05``, create a function named ``student_report()``

    #.  ``student_report()`` should take 3, required, keyword arguments:

        #.  ``name``

        #.  ``age``

        #.  ``school_id``

    #.  ``student_report()`` may also take additional, magic, keyword
        arguments.

    #.  All arguments should be included in a single dictionary keyed by the
        argument name.

    #.  Return the created dictionary.

Examples
^^^^^^^^

.. code:: pycon

    >>> mass_multiplier(1, 2)
    2

    >>> mass_multiplier(1, 2, 3, 6, 98, 0)
    0

    >>> student_report(name='Jane', age=13, school_id='ps-1')
    {'name': 'Jane', 'age': 3, 'school_id': 'ps-1')

    >>> student_report(name='Jane', age=13, school_id='ps-1', math='B')
    {'name': 'Jane', 'age': 3, 'school_id': 'ps-1', 'math'=B)

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Lesson 01.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
.. _Unix Timestamp: https://en.wikipedia.org/wiki/Unix_time
