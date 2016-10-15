Hijri Calendar Converter
========================

.. image:: https://travis-ci.org/QuantumPrayerTimes/hijricalendar.svg?branch=master
    :alt: Build
    
.. image:: https://coveralls.io/repos/github/QuantumPrayerTimes/hijricalendar/badge.svg?branch=master
    :target: https://coveralls.io/github/QuantumPrayerTimes/hijricalendar?branch=master

.. image:: https://landscape.io/github/QuantumPrayerTimes/hijricalendar/master/landscape.svg?style=flat
    :target: https://landscape.io/github/QuantumPrayerTimes/hijricalendar/master
    :alt: Code Health
    
.. image:: https://codecov.io/gh/QuantumPrayerTimes/hijricalendar/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/QuantumPrayerTimes/hijricalendar

.. image:: https://codeclimate.com/github/QuantumPrayerTimes/hijricalendar/badges/gpa.svg
    :target: https://codeclimate.com/github/QuantumPrayerTimes/hijricalendar
    :alt: Code Climate

.. image:: https://codeclimate.com/github/QuantumPrayerTimes/hijricalendar/badges/coverage.svg
    :target: https://codeclimate.com/github/QuantumPrayerTimes/hijricalendar/coverage
    :alt: Test Coverage

.. image:: https://www.quantifiedcode.com/api/v1/project/4474c9b2f12f498c9defecaf6a958932/badge.svg
   :target: https://www.quantifiedcode.com/app/project/4474c9b2f12f498c9defecaf6a958932
   :alt: Code issues

Python Umalqurra Calender is an API that will give you the ability to convert Gregorian to Hijri and hijri to
Gregorian. It will give you the day name in arabic and english, and the month name in Hijri arabic and Gregorian.

The Hijri algorithm code has been translatde from javascript to python.

The javascript was developed by Suhail Alkowaileet:
https://github.com/xsoh/Hijri.js/blob/master/Hijri.js

also this code for more understanding:
https://github.com/kbwood/calendars/blob/master/src/js/jquery.calendars.ummalqura.js

The project is based on : https://github.com/tytkal/python-hijiri-ummalqura

Compatibility:
Compatible with Python 2.x and 3.x

**This is an improved version PEP8 compliant, bugs fixed and ready to use.**

Prerequisites
=============

You will need the following software properly installed on your computer.

* `Git <http://git-scm.com/>`__
* `Python 2.x or 3.x <https://www.python.org/>`__

Installation
============

Clone the repo and run :

.. code:: python

    git clone https://github.com/QuantumPrayerTimes/hijricalendar.git
    cd hijricalendar
    python setup.py install

Usage
=====

Example of usage :

.. code:: python

    import datetime
    from hijricalendar.hijri_date_wrap import HijriDateWrapper

    today = datetime.date.today()

    # Create a gregorian date
    hdw = HijriDateWrapper(date=today, gregorian=True)
    print(hdw)

    # Get the associated Hijri date
    hdw.get_hijri_date()
    hdw.get_gregorian_date()

    # Set the date to another one
    hdw.set_date_from_gr(2016, 10, 15)
    hdw.get_hijri_date()
    hdw.get_gregorian_date()

    # Set a Hijri date
    hdw.set_date_from_hr(1437, 10, 15)
    hdw.get_hijri_date()
    hdw.get_gregorian_date()

Resources
=========
* Homepage: https://github.com/QuantumPrayerTimes/hijricalendar
* Source:

    - Browse at https://github.com/QuantumPrayerTimes/hijricalendar


Issues
======

If you have any issues or improvements, do not hesitate to create an
issue or submit a pull request.
