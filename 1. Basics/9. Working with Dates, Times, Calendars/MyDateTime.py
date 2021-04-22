from datetime import date
from datetime import datetime

today = date.today()

print("Today is ", today)
print("The date components are", today.day, today.month, today.year)
print("The weekday number is", today.weekday())

days = ["mon", "tues", "wed", "thu", "fri", "sat", "sun"]
print("The weekday is", days[today.weekday()])

current_time = datetime.now()
print("The current time is", current_time)

only_time = datetime.time(current_time)
print("The time now is", only_time)
