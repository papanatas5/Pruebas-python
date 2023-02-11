### Datos ###

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.microsecond)
    print(date.timestamp())

print_date(now)

year_2024 = datetime(2024, 1, 1)

print_date(year_2024)

from datetime import time

current_time = time(15, 46, 2)

print (current_time.hour)
print (current_time.minute)
print (current_time.second)

from datetime import date

current_date = date.today()

print (current_date.year)
print (current_date.month)
print (current_date.day)
#print (current_date.weekday)

current_date = date(2023, 2, 1)

print (current_date.year)
print (current_date.month)
print (current_date.day)

current_date = date(current_date.year, current_date.month +1, current_date.day)

print (current_date.month)

#diferencia
diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date
print(diff)

print(year_2024.time())

#timedelta
from datetime import timedelta

start_timedelta = timedelta(250, 48, 100, weeks = 5)
end_timedelta = timedelta(250, 48, 100, weeks = 7)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
