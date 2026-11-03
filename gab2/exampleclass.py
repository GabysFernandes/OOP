'''from datetime import date, time, datetime, timezone, timedelta

print(date.today())
print(datetime.now())
print(timedelta(days=3, hours=2))'''


'''from datetime import datetime, timezone
local_now = datetime.now().astimezone()
utc_now = local_now.astimezone(timezone.utc)
print("Local: ", local_now)
print("UTC: ", utc_now)'''


'''from datetime import datetime, timezone
local = datetime.now().astimezone()
utc = local.astimezone(timezone.utc)
print("Local: ", local.isoformat())
print("UTC: ", utc.isoformat())
print("Same instant? ", local == utc)'''


'''from datetime import datetime

now = datetime(2026, 11, 2, 9, 30)

print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A, %d %B %Y"))
print(now.strftime("%H:%M"))'''

'''
from datetime import datetime

text = "2026-12-31 23:59"

try:
    result = datetime.strptime(text, "%Y-%m-%d %H:%M")
    print("Parsed:", result)
except ValueError:
    print("Invalid date or time")'''

'''
from datetime import datetime, timedelta

start = datetime(2026, 11, 2, 9, 0)
duration = timedelta(days=2, hours=3, minutes=30)
deadline = start + duration

print(deadline.strftime("%d/%m/%Y %H:%M"))
# 04/11/2026 12:30'''


'''
from datetime import date

start = date(2026, 12, 24)
end = date(2026, 12, 25)

difference = end - start

print(difference)        # 1 day, 0:00:00
print(difference.days)   # 1'''


'''
from datetime import date

def days_until_christmas():
    today = date.today()
    christmas = date(today.year, 12, 25)

    if today > christmas:
        christmas = date(today.year + 1, 12, 25)

    return (christmas - today).days

print("Days remaining:", days_until_christmas())'''

'''
from datetime import date
def days_until_birthday(month, day):
    today = date.today()
    birthday = date(today.year, month, day)

    if birthday < today:
        birthday = date(today.year + 1, month, day)

    return (birthday - today).days

print(days_until_birthday(2, 23))
'''

from datetime import date

class EventCountdown:
    def __init__(self, event_date: date):
        self.event_date = event_date

    def get_days_remaining(self):
        today = date.today()
        return (self.event_date - today).days


event = EventCountdown(date(2027, 6, 14))
print(event.get_days_remaining())