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

This is an API for Hijri Umalqurra Calendar,
It was developed  by khalid Al-hussayen 1436-3-15 2015-1-6.

The algorithm of converting hijri to  Gregorian is in hijri.py

This Api will give the ability to convert Gregorian To Hijri or Hijri to Gregorian with the day and month
names in Hijri and Gregorian

You can query for the current day in both Hijri and Gregorian
"""

import datetime

from hijricalendar.hijri import gregorian_to_hijri, hijri_to_gregorian


class HijriDateWrapper:
    """
    HijriDateWrapper is a class that make easy the use of Hijri Umalqurra Calendar API.
    """

    # Date in Hijri
    day_hr = None
    month_hr = None
    year_hr = None

    # Date in Gregorian
    day_gr = None
    month_gr = None
    year_gr = None

    month_dict = {1: 'محرم',
                  2: 'صفر',
                  3: 'ربيع الأول',
                  4: 'ربيع الثاني',
                  5: 'جمادي الأولى',
                  6: 'جمادي الآخرة',
                  7: 'رجب',
                  8: 'شعبان',
                  9: 'رمضان',
                  10: 'شوال',
                  11: 'ذو القعدة',
                  12: 'ذو الحجة'}

    day_dict = {'Saturday': 'السبت',
                'Sunday': 'الاحد',
                'Monday': 'الاثنين',
                'Tuesday': 'الثلاثاء',
                'Wednesday': 'الاربعاء',
                'Thursday': 'الخميس',
                'Friday': 'الجمعة'}

    # Day and month in English
    en_month_name = ''
    en_day_name = ''

    # Day and month in Arabic
    ar_day_name = ''
    ar_month_name = ''

    def __init__(self, date=datetime.date.today(), gregorian=True):
        """
        Initialize the date depending on parameter.
        :param date:
        :param gregorian:
        """
        if not isinstance(date, datetime.date):
            raise ValueError("Please provide a date object from datetime module")
        if not gregorian:
            # Set the Hijri date to convert
            self.set_date_from_hr(date.year, date.month, date.day)
        else:
            # Set the Gregorian date to convert
            self.set_date_from_gr(date.year, date.month, date.day)

    def set_date_from_gr(self, year, month, day):
        """
        Provide the date in Gregorian format.
        Every parameter is then updated.
        :param year:
        :param month:
        :param day:
        :return:
        """
        self.year_gr, self.month_gr, self.day_gr = year, month, day

        # Convert to Hijri date
        self.year_hr, self.month_hr, self.day_hr = gregorian_to_hijri(year, month, day)

        # Get the english and arabic name of the day
        date_gr = datetime.date(year, month, day)
        self.en_day_name = date_gr.strftime("%A")
        self.ar_day_name = self.day_dict[self.en_day_name]
        self.en_month_name = date_gr.strftime("%B")

        # Map the Hijri month calculated with its arabic name
        self.ar_month_name = self.month_dict[self.month_hr]

    def set_date_from_hr(self, year, month, day):
        """
        Provide the date in Hijri format.
        Every parameter is then updated.
        :param year:
        :param month:
        :param day:
        :return:
        """
        self.year_hr, self.month_hr, self.day_hr = year, month, day

        # Convert to Gregorian date
        self.year_gr, self.month_gr, self.day_gr = hijri_to_gregorian(year, month, day)

        # Get the english and arabic name of the day
        date_gr = datetime.date(int(self.year_gr), int(self.month_gr), int(self.day_gr))
        self.en_day_name = date_gr.strftime("%A")
        self.ar_day_name = self.day_dict[self.en_day_name]
        self.en_month_name = date_gr.strftime("%B")

        # Map the Hijri month calculated with its arabic name
        self.ar_month_name = self.month_dict[month]

    def get_hijri_date(self):
        """
        Print formatted date in Hijri format:
        e.g. الاحد 10 ذو الحجة 1432
        :return:
        """
        hijri_date = "{0} {1} {2} {3}".format(self.ar_day_name, self.day_hr, self.ar_month_name, self.year_hr)
        print(hijri_date)
        return hijri_date

    def get_gregorian_date(self):
        """
        Print formatted date in Gregorian format:
        e.g. Sunday 6 November 2011
        :return:
        """
        gregorian_date = "{0} {1} {2} {3}".format(self.en_day_name, self.day_gr, self.en_month_name, self.year_gr)
        print(gregorian_date)
        return gregorian_date

    def __str__(self):
        return self.get_hijri_date()
