from datetime import datetime

today = datetime.now()

time24 = today.strftime('%H')
time12 = today.strftime('%I')
timeM = today.strftime("%M")
timeS = today.strftime("%S")
timeMili = today.strftime("%f")
amPM = today.strftime('%p')
UTC = today.strftime("%z")
TimeZone = today.strftime("%Z")

dayY = today.strftime("%j")
week_monY = today.strftime("%W")
week_sunY = today.strftime("%U")
local_version_time_date = today.strftime("%c")
local_version_time = today.strftime("%X")
local_version_date = today.strftime("%x")


def SpaceX(msg):
    space = "________".join("-------------------")
    print(space)
    print(msg)
    print(space)


if __name__ == "__main__":
    SpaceX("Now playing with your date...")

    text = "Your date information "
    print(today.strftime(text + "(short): " + "%a, %dth %b, %y"))
    print(today.strftime(text + "(full): " + "%A, %dth %B, %Y"))
    print(today.strftime("Month number: %m"))

    SpaceX("Now playing with your time...")

    print(f"Time is 24 format:\n {UTC} {TimeZone} {time24} : {timeM} : {timeS} : {timeMili}")
    print(f"Time is 12 format:\n {UTC} {TimeZone} {time12} : {timeM} : {timeS} : {timeMili} ({amPM})")

    SpaceX("Now playing with your date & time...")

    print(f"Number of the day of this year is: {dayY}")
    print(f"Number of the week (Monday) of this year is: {week_monY}")
    print(f"Number of the week (Sunday) of this year is: {week_sunY}")
    print(f"Local time is: \n{local_version_time}")
    print(f"Local date is: \n{local_version_date}")
    print(f"\nAgain, Local date & time is: \n{local_version_time_date}")
