MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


class ImprovedTimeDelta():
    def __init__(self, from_date, to_date):
        if to_date < from_date:
            raise Exception("to_date should be later than from_date")
        self.to_date = to_date
        self.from_date = from_date
        self.diff = to_date - from_date

    def __str__(self):
        d = self.days()
        months, days = self._get_months(d)
        years = self._get_years()
        return "%d Years, %d Months, %d Days" % (years, months, days)

    def add_on_if_leap(self, month_day_count, date_obj):
        if is_leap_year(date_obj.year):
            if date_obj.month == 2:
                return month_day_count + 1
        return month_day_count

    def _get_months(self, d):

        if self.from_date.month == self.to_date.month:
            if self.from_date.day == self.to_date.day:
                return 0, 0
            if self.to_date.day > self.from_date.day:
                return 0, self.to_date.day - self.from_date.day

        if self.from_date.day == self.to_date.day:
            if self.from_date.month > self.to_date.month:
                return ((self.to_date.month + 12) - (self.from_date.month)), 0
            else:
                return (self.to_date.month - self.from_date.month), 0
        start_month_day_count = MONTHS[self.from_date.month - 1]
        start_month_day_count = self.add_on_if_leap(start_month_day_count,
                self.from_date)

        start_date = self.from_date.day
        # days at start, plus 1 to include the current day
        remaining_days = (start_month_day_count - start_date + 1)
        end_date = self.to_date.day
        remaining_days += end_date

        month_count = 0
        month_iterator = self.from_date.month + 1
        while self.month_stop(month_iterator):
            month_count += 1
            month_iterator += 1
            if month_iterator == 12:
                month_iterator = 1

        return month_count, remaining_days

    def month_stop(self, month_iterator):
        if month_iterator == self.to_date.month:
            return False
        if month_iterator == self.from_date.month:
            return False
        return True

    def days(self):
        return self.diff.days

    def _get_years(self):
        years = (self.to_date.year - self.from_date.year)
        if self.to_date.month > self.from_date.month:
            return years
        elif self.to_date.month < self.from_date.month:
            return years - 1
        else:
            if self.to_date.day < self.from_date.day:
                return years - 1
            else:
                return years
