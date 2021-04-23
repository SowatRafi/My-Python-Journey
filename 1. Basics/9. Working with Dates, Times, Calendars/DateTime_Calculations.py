from datetime import date
from datetime import datetime
from datetime import timedelta

thisDay = datetime.now()

# Calculating in the future
print(str(thisDay + timedelta(365)))
# print(timedelta(days=365, hours=7, minutes=7))
print(str(thisDay + timedelta(days=4, weeks=5)))

# Calculate in past
x = datetime.now() - timedelta(weeks=10)
y = x.strftime("%c")
print(y)

# Days-left calculator
daysAhead = date.today()
birthday = date(year=daysAhead.year, month=int(input("\nEnter your birthday month\n")), day=int(input("Enter your birthday date\n")))
timeToBirthday = birthday - daysAhead
print(f"{timeToBirthday.days} left for your birthday")