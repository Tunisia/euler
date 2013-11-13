#!/usr/bin/python

#You are given the following information, but you may prefer to do some research for yourself.
#
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def date(dayofweek = 1,dayofmonth=1,month=1,year=2013):
    while True:
        yield (dayofweek, dayofmonth, month, year)
        dayofweek += 1
        dayofmonth += 1
        if dayofweek > 7:
            dayofweek = 1
        if dayofmonth > 28:
            if month in [4,6,9,11]:
                if dayofmonth > 30:
                    dayofmonth = 1
                    month += 1
            elif month in [1,3,5,7,8,10,12]:
                if dayofmonth > 31:
                    dayofmonth = 1
                    month += 1
            elif month == 2:
                if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
                    if dayofmonth > 29:
                        dayofmonth = 1
                        month += 1
                else:
                        dayofmonth = 1
                        month += 1
        if month > 12:
            month = 1
            year += 1

d = date(1,1,1,1900)

day = d.next()
count = 0

while day[3] < 2001:
    day = d.next()
    
    if day[3] > 1900 and day[0] == 7 and day[1] == 1:
        count = count + 1

print count