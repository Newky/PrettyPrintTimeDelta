import unittest

from datetime import datetime
from timedelta import PrettyPrintTimeDelta


class TimeDeltaTest(unittest.TestCase):
    def test_one_day(self):
        x = datetime(2012, 01, 01)
        y = datetime(2012, 01, 02)
        td = PrettyPrintTimeDelta(x, y)
        self.assertEquals(str(td), "0 Years, 0 Months, 1 Days")

    def test_one_month(self):
        x = datetime(2012, 01, 01)
        y = datetime(2012, 02, 01)
        td = PrettyPrintTimeDelta(x, y)
        self.assertEquals(str(td), "0 Years, 1 Months, 0 Days")

    def test_one_year(self):
        x = datetime(2012, 01, 01)
        y = datetime(2013, 01, 01)
        td = PrettyPrintTimeDelta(x, y)
        self.assertEquals(str(td), "1 Years, 0 Months, 0 Days")

    def test_one_year_and_one_month(self):
        x = datetime(2012, 01, 01)
        y = datetime(2013, 02, 01)
        td = PrettyPrintTimeDelta(x, y)
        self.assertEquals(str(td), "1 Years, 1 Months, 0 Days")

    def test_less_than_year_but_cross_years(self):
        x = datetime(2012, 02, 01)
        y = datetime(2013, 01, 01)
        td = PrettyPrintTimeDelta(x, y)
        self.assertEquals(str(td), "0 Years, 11 Months, 0 Days")

    def test_less_than_2year_but_cross_months(self):
        x = datetime(2012, 02, 01)
        y = datetime(2014, 01, 01)
        td = PrettyPrintTimeDelta(x, y)
        self.assertEquals(str(td), "1 Years, 11 Months, 0 Days")

    def test_less_than_2year_and_cross_months(self):
        x = datetime(2012, 03, 30)
        y = datetime(2014, 02, 04)
        td = PrettyPrintTimeDelta(x, y)
        self.assertEquals(str(td),"1 Years, 9 Months, 6 Days")

    def test_less_than_2year_same_month(self):
        x = datetime(2012, 03, 06)
        y = datetime(2014, 03, 04)
        td = PrettyPrintTimeDelta(x, y)
        self.assertEquals(str(td),"1 Years, 10 Months, 30 Days")

    def test_not_a_leap_year(self):
        # leap year test
        # first with not a leap year
        x = datetime(2013, 02, 06)
        y = datetime(2013, 04, 03)
        td = PrettyPrintTimeDelta(x, y)
        self.assertEquals(str(td),"0 Years, 1 Months, 26 Days")

    def test_leap_year(self):
        x = datetime(2012, 02, 06)
        y = datetime(2012, 04, 03)
        td = PrettyPrintTimeDelta(x, y)
        self.assertEquals(str(td),"0 Years, 1 Months, 27 Days")

    def test_simple_subtraction(self):
        x = datetime(2012, 02, 12)
        y = datetime(2013, 06, 13)
        td = PrettyPrintTimeDelta(x, y)
        self.assertEquals(str(td),"1 Years, 4 Months, 1 Days")


if __name__ == "__main__":
    unittest.main()
