**Formatting Date and Time**

* The datetime object has a method for formatting date objects into readable strings. It is called `strtime()`
* It takes one parameter, format to specify the format of the Returned string.

**Formatting Date**

`%a` - Weekday short version - _Mon_

`%A` - Weekday full version - _Monday_

`%w` - Weekday index numbers 0-6 : **Mon is index 0** - _0_

`%d` - Day of the month - _17_

`%b` - Month name short version - _Aug_

`%B` - Month name full version - _August_

`%m` - Month as number: **01 - 12** - _8_

`%y` - Year short version, without century - _21_

`%Y` - Year full version - _2021_


**Formatting Time**

`%H` - Hour: **00 - 23** - _18_

`%I` - Hour: **00 - 12** - _7_

`%p` - **AM | PM** - _AM_

`%M` - Minute: **00 - 59** - _47_

`%S` - Seconds: **00 - 58** - _07_

`%f` - Microsecond: **000000 - 999999** - _23486_

`%z` - **UTC** offset - _+06_

`%Z` - TimeZone - _GMT_

`%j` - Day number of year: **001 - 366** - _365_

`%U` - Week number of year. **Sunday** as the first day of the week **00 - 53** - _52_

`%W` - Week number of year. **Monday** as the first day of the week **00 - 53** - _52_

`%c` - Local version of date & time - _Fri Apr 23 2:33:04:24 2021_

`%x` - Local version of date - _04|23|21_

`%X` - Local version of time - _14:20:00_

`%%` - A % character - _%_
