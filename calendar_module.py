import datetime
import calendar

print(calendar.TextCalendar(firstweekday=6).formatyear(2020))

month, day, year = map(int, input().split())
my_date = datetime.date(year, month, day)
print(calendar.day_name[my_date.weekday()].upper())




