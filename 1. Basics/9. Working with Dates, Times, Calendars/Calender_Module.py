import calendar


def SpaceX(msg):
    space = "________".join("-------------------")
    print(space)
    print(msg)
    print(f"{space}\n")


cal = calendar.TextCalendar(calendar.SATURDAY)

SpaceX("%20s" % "Texted based")

text = cal.formatmonth(2001, 5)
print(text)

SpaceX("%20s" % "HTML based Calender")
cal = calendar.HTMLCalendar(calendar.SATURDAY)
html = cal.formatmonth(1999, 12)
print(html)

SpaceX("%20s" % "In the output: The 0's are the days from another month")

for days in cal.itermonthdays(year=2021, month=8):
    print(days)

SpaceX("%20s" % "Month names")

for name in calendar.month_name:
    print(name)

SpaceX("Day names")

for name in calendar.day_name:
    print(name)

SpaceX("%20s" % "Script for the meeting")

print("\nTeam meeting will be on (1st monday of the month):")
"""
Loops though range and returns 1-12 months.
"""
for m in range(1, 13):
    """
    The `monthcalendar` function returns an list of weeks that represent the month.
    """
    cal = calendar.monthcalendar(year=2021, month=m)
    """
    To return the first week in the list from the cal variable we pass in the index of the week 1 which is 0 into 
    the `week1` cal list value.
    The index of `week2` variable will be 1.
    """
    week1 = cal[0]
    week2 = cal[1]
    """
       If the first monday is not = 0 that means it falls on the first week of the month. So the code for
       variable meeting inside the if blocked will be called.
    """
    if week1[calendar.MONDAY] != 0:
        meeting = week1[calendar.MONDAY]
        """
        If the first Monday of each month falls on the second week then the else block code in the meeting variable 
        for variable week2 will be called to execute.
        """
    else:
        meeting = week2[calendar.MONDAY]

    print("%10s %d" % (calendar.month_name[m], meeting))

SpaceX("%60s" % "The End")
