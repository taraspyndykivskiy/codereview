"""
Перше січня першого року нашої ери було понеділком за сучасним грегоріанським календарем.
Користувач вводить дату у форматі `31-12-0001`.
Напишіть функцію, що повертає день тижня, на який припадає ця дата.
Виведіть результат.
У випадку помилкового вводу виведіть повідомлення про помилку.
(Припускайте однорідність календаря і відсутність додаткових днів, окрім високосних років.)
"""

import re

pattern=re.compile(r"\d{1,2}-\d{1,2}-\d{4}")

def validator(enter, pattern):
    data=date_validator(enter, pattern)
    return data

def date_validator(enter, pattern):
    date=input(enter)
    while not bool(pattern.findall(date)[0]):
        date = input(enter)
    return date

real_date=str(validator("enter the date format ", pattern))
real_date=(real_date.split("-"))
numeric_format=[int(j) for j in real_date]

high_year=False
if numeric_format[2]%4==0:
    high_year=True

high_year_monthly=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
usual_year_monthly=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date_number=0

for i in range (numeric_format[1]-1):
    if(high_year==True):
        date_number+=high_year_monthly[i]
    else:
        date_number += usual_year_monthly[i]

date_number+=numeric_format[0]



day_week=date_number%7

days_of_week=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

print("your day of the week is "+str(days_of_week[day_week]))