from datetime import datetime
strptime = datetime.strptime
f = "%d.%m.%Y"


def diff(date1, date2):
    return abs(strptime(date1, f) - strptime(date2, f)).days/365


dates = "11.11.2016", "12.04.2018"  # y
dates = "01.03.2019", "24.08.2015"  # n
dates = "13.11.2017", "24.08.2015"  # n
dates = "19.10.1988", "22.12.1991"  # n
dates = "12.05.1998", "22.12.1991"  # n
dates = "17.06.1993", "22.12.1991"  # y
dates = "09.05.1967", "14.07.1961"  # n
dates = "09.05.1967", "14.07.1961"  # n
dates = "08.09.1971", "14.07.1961"  # n
dates = "09.05.1967", "08.09.1971"  # n

print(diff(*dates))
