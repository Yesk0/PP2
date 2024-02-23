import datetime

date = datetime.datetime.now()

old_date = datetime.datetime(date.year, date.month, date.day - 5)
print("date 5 days ago:", old_date.strftime("%d %B %Y"))