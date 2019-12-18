#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar making Sunday the first day of the week
c = calendar.TextCalendar(calendar.SUNDAY)
#formats a particular month into a text string
# st = c.formatmonth(2019, 12, 0, 0)
# #prints results
# print(st)

# # create an HTML formatted calendar making Sunday the first day of the week
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2019, 12)
# print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2019, 8):
#     print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on: ")
for m in range(1,13):
    cal = calendar.monthcalendar(2019, m)
    weekone=cal[0]
    weektwo=cal[1]
    
    #conditions to determine if the first friday of the month
    #is in the first or second week
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    
    print("%10s %2d" % (calendar.month_name[m], meetday))