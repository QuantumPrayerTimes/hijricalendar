#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
------------------------ Copyright Block -----------------------

Calendar converter improved by Sid-Ali TEIR.

License: GNU LGPL v3.0

TERMS OF USE:
* Permission is granted to use this code, with or
* without modification, in any website or application
* provided that credit is given to the original work
* with a link back to PrayTimes.org.

This program is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY.

PLEASE DO NOT REMOVE THIS COPYRIGHT BLOCK.

------------------------ Help and Manual ------------------------

This class is responsoble to convert from Hijri to Gregorian or from Gregorian to Hijri

The algorithm was converted  from java script to python by Khalid Al-hussayen in 1436-3-14 2015-1-5

The orjinal source developed by Suhail Alkowaileet the source url :
https://github.com/xsoh/Hijri.js/blob/master/Hijri.js
"""

import math

from hijricalendar.ummalqura_arrray import UmalqurraArray


def gregorian_to_hijri(year, month, day):
    """
    Convert Gregorian date to Hijri date.
    This code the modified version of R.H. van Gent Code, it can be found at :
    http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm
    read calendar data
    :param year:
    :param month:
    :param day:
    :return:
    """

    day = int(day)
    m = int(month)  # Here we enter the Index of the month (which starts with Zero)
    y = int(year)

    # Append January and February to the previous year (i.e. regard March as
    # the first month of the year in order to simplify leapday corrections)
    if m < 3:
        y -= 1
        m += 12

    # Determine offset between Julian and Gregorian calendar
    a = math.floor(y / 100.)
    jgc = a - math.floor(a / 4.) - 2

    # Compute Chronological Julian Day Number (CJDN)
    cjdn = math.floor(365.25 * (y + 4716)) + math.floor(30.6001 * (m + 1)) + day - jgc - 1524

    # a = math.floor((cjdn - 1867216.25) / 36524.25)

    # Compute Modified Chronological Julian Day Number (MCJDN)
    mcjdn = cjdn - 2400000

    # The MCJDN's of the start of the lunations in the Umm al-Qura calendar are stored in 'ummalqura_arrray.py'
    index = UmalqurraArray.get_index(mcjdn)

    # Compute and output the Umm al-Qura calendar date
    iln = index + 16260
    ii = math.floor((iln - 1) / 12)
    iy = ii + 1
    im = iln - 12 * ii
    id_ = mcjdn - UmalqurraArray.ummalqura_dat[index - 1] + 1
    return iy, im, id_


def hijri_to_gregorian(year, month, day):
    """
    Convert Hijri date to Gregorian date.
    :param year:
    :param month:
    :param day:
    :return:
    """

    year = int(year)
    month = int(month)
    day = int(day)
    iy = year
    im = month
    id_ = day
    ii = iy - 1
    iln = (ii * 12) + 1 + (im - 1)
    i = iln - 16260
    mcjdn = id_ + UmalqurraArray.ummalqura_dat[i - 1] - 1
    cjdn = mcjdn + 2400000
    return julian_to_gregorian(cjdn)


def julian_to_gregorian(julian_date):
    """
    Convert Julian date to Gregorian date.
    Source from: http://keith-wood.name/calendars.html
    :param julian_date:
    :return:
    """

    z = math.floor(julian_date + 0.5)
    a = math.floor((z - 1867216.25) / 36524.25)
    a = z + 1 + a - math.floor(a / 4)
    b = a + 1524
    c = math.floor((b - 122.1) / 365.25)
    d = math.floor(365.25 * c)
    e = math.floor((b - d) / 30.6001)
    day = b - d - math.floor(e * 30.6001)

    if e > 13.5:
        month = e - 13
    else:
        month = e - 1
    if month > 2.5:
        year = c - 4716
    else:
        year = c - 4715
    if year <= 0:
        year -= 1
    return year, month, day
