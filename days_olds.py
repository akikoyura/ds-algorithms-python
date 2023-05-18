daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_in_month(year, month):
    if is_leaf_year(year) and month == 2:
        return 29
    else:
        return daysOfMonths[month - 1]


def next_day(year, month, day):
    days = days_in_month(year, month)
    if day < days:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


def date_is_before(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def is_leaf_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    return False


def days_between_dates(year1, month1, day1, year2, month2, day2):
    days = 0
    if not date_is_before(year1, month1, day1, year2, month2, day2):
        return days
    while date_is_before(year1, month1, day1, year2, month2, day2):
        days += 1
        year1, month1, day1 = next_day(year1, month1, day1)

    return days


def test_days_between_dates():
    # test same day
    assert (days_between_dates(2017, 12, 30, 2017, 12, 30) == 0)
    # # test adjacent days
    assert (days_between_dates(2017, 12, 30, 2017, 12, 31) == 1)
    # test new year
    assert (days_between_dates(2017, 12, 30, 2018, 1, 1) == 2)
    # test full year difference
    assert (days_between_dates(2012, 6, 29, 2013, 6, 29) == 365)
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


if __name__ == '__main__':
    test_days_between_dates()
