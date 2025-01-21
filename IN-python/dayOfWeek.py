ntuition
# Let us consider the odd days in the given year. As the test cases renge is from 1970
#  to 2100 so we can choose a year before 1970 and which comes after leap year.
#  So we can take 1969 which has 3 odd days. Then subtract the given year by 1969
#  then store it in diff_y which is difference of years. For leap years present in
#  between the given year and 1969 odd days is 2 and for non-leap years it is 1. 
# So we use another variable leap_y stores the leap years by floor division of diff_y.
#  Then store the odd days of years in odd_days.

# Then create a days list in which it contains the days name in order starts from Sunday to Saturday and the odd days represent the index number of list days. Then create another list l which stores the number of days in a month. Then loop it till month-1 and add it to odd_days. Finally add the number of days to the odd_days and return the days modulus of 7 which represents the index value of days and returns the corrresponding day of the given date which is in range year greater than 1969.

# Approach
# Complexity
# Time complexity: O(month)
# Space complexity: O(1)
# Code
# class Solution:
#     def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
#         days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
#         diff_y=abs(year-1969)
#         leap_y=diff_y//4
#         odd_days=leap_y*2+(diff_y-leap_y)+2
#         l=[31,28,31,30,31,30,31,31,30,31,30,31]
#         if year%400==0 or (year%4==0 and year%100!=0) :
#             l[1]=29
#         for i in range(month-1):
#             odd_days+=l[i]
#         odd_days+=day
#         return days[odd_days%7]

from datetime import datetime
def dayOfWeek(day,month,year):
    
    date = datetime(year, month, day)
    
    # Get the day of the week as a string
    return date.strftime("%A")

# day = 31, month = 8, year = 2019
print(dayOfWeek(18,7,1999))