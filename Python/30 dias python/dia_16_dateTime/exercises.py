# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime, timedelta
now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timeStamp = now.timestamp()

print("el dia es{}, mes {}, año {}, y la hora es {} con {} minutos y {}".format(
    day, month, year, hour, minute, second))
print(timeStamp)
print()

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
time_format = now.strftime("%d/%m/%Y, %H:%M:%S")
print(time_format)
print()

# Today is 5 December, 2019. Change this time string to time.
date_str = "31 October, 2022"
date_obj = datetime.strptime(date_str, "%d %B, %Y")
print(date_obj)
print()

# Calculate the time difference between now and new year.
t1 = timedelta(days=3, hours=16, minutes=22, seconds=30)
t2 = timedelta(days=day, hours=hour, minutes=minute, seconds=second)
t3 = t2 - t1
print("t1 =", t1)
print("t2 =", t2)
print("diference =", t3)
print()

# Think, what can you use the datetime module for? Examples:
'''
Time series analysis
To get a timestamp of any activities in an application
Adding posts on a blog

relog 
calendario
'''
