#!/usr/bin/python
#IFT 383 Term B Fall 2019
#Extra Credit Assingment

#https://www.w3resource.com/python-exercises/python-basic-exercise-14.php
from datetime import date
from datetime import datetime

#get today's date
today = datetime.today() 

newYearsDate = date(today.year, 1, 1)
mlkDate = date(today.year, 1, 20)
washingtonBday = date(today.year, 2, 17)
memorialDayDate = date(today.year, 5, 25)
independenceDayDate = date(today.year, 7, 4)
laborDayDate = date(today.year, 9, 7)
columbusDayDate = date(today.year, 10, 12)
veteransDayDate = date(today.year, 11, 11)
thanksgivingDate = date(today.year, 11, 26)
christmasDate = date(today.year, 12, 25)

dateArray = [newYearsDate, mlkDate, washingtonBday,
    memorialDayDate, independenceDayDate, laborDayDate,
    columbusDayDate, veteransDayDate, thanksgivingDate, christmasDate]

#will return the first holiday that meets the condition. This is the next holiday.
def findNextHoliday():
    for date in dateArray:
        if (today.month <= date.month):
            if (today.day <= date.day):
                return date

nextHoliday = findNextHoliday()

#need to convert both objects to date to calculatet the timedelta
timeTillHoliday = nextHoliday - today.date()
#formats the string to only get what we want. 
dayString = str(timeTillHoliday).split(",")[0] 
print("There is only %s till the next holiday" %dayString)


