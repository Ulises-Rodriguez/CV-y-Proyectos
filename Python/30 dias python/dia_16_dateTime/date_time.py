# Date Time

# import datetime
# print(dir(datetime))
# With dir or help built-in commands it is possible to know the available functions in a certain module. As you can see, in the datetime module there are many functions, but we will focus on date, datetime, time and timedelta. Let se see them one by one.
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#     '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']


# obtener date time info
from datetime import datetime, date, time, timedelta

now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second

# Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.
timestamp = now.timestamp()

print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')
print()

# strftime --> https://strftime.org/
# método devuelve una cadena que representa la fecha y la hora mediante el objeto date , time o datetime

new_year = datetime(2022, 1, 1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)  # 1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')
print()

# formatear date time con strftime
now = datetime.now()  # fecha actual
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)
print()


# pasar de string a date time con strptime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
print()

# usando date para obtener dateTime
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month)  # 12
print("Current day:", today.day)
print()

# objeto time para representar el timepo
a = time()
print("a =", a)
# horas minutos segundo
b = time(10, 30, 50)
print("b =", b)
# otra forma
c = time(hour=10, minute=30, second=50)
print("c =", c)
# horas minutos segundo microsegundos
d = time(10, 30, 50, 200555)
print("d =", d)
print()

# timedelta --> diferencias de tiempo entre una fecha y otra
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
print()
