#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import unittest

from hijricalendar.hijri_date_wrap import HijriDateWrapper
from hijricalendar.hijri import gregorian_to_hijri, hijri_to_gregorian


class TestPT(unittest.TestCase):
    """
    Unittest.
    """

    DATE = datetime.date.today()

    def setUp(self):
        """
        setUp is the initializaion of variables needed in tests.
        """

        self.hdw = HijriDateWrapper(date=self.DATE, gregorian=True)
        print(self.hdw)

    def test_instance_test(self):
        """
        Verify the instance of each variables needed.
        """

        self.assertTrue(isinstance(self.hdw, HijriDateWrapper))
        self.assertTrue(isinstance(self.hdw.get_gregorian_date(), str))
        self.assertTrue(isinstance(self.hdw.get_hijri_date(), str))

    def test_running(self):
        """
        Run the tests concerning integrity.
        """

        self.hdw.get_hijri_date()
        self.hdw.get_gregorian_date()

        self.hdw.set_date_from_gr(2016, 10, 15)
        self.hdw.get_hijri_date()
        self.hdw.get_gregorian_date()

        self.hdw.set_date_from_hr(1437, 10, 15)
        self.hdw.get_hijri_date()
        self.hdw.get_gregorian_date()

        date = datetime.date.today()
        gregorian_to_hijri(date.year, date.month, date.day)
        hijri_to_gregorian(1437, 10, 22)


if __name__ == '__main__':
    unittest.main()
