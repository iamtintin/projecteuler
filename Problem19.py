"""
Find the first day which is a Sunday
then find the difference in days to the next first day of a month
to find what day it is on the first of a month find the remainder when dividing the difference by 7
0 - Sunday
1 - Monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - Friday
6 - Saturday

1st January 1901 was a Tuesday

"""

months31 = [1, 3, 5, 7, 8, 10, 12]
months30 = [4, 6, 9, 11]

startYear = 1901
finishYear = 2000
countSundays = 0
day = 2

for year in range(startYear, finishYear+1):
    for month in range(1,13):
        if month in months31:
            daysInMonth = 31
        elif month in months30:
            daysInMonth = 30
        elif month == 2:
            if year % 4 == 0: 
                daysInMonth = 29
            else:
                daysInMonth = 28
        day = (day + daysInMonth) % 7
        if day == 0:
            countSundays += 1

print(countSundays)