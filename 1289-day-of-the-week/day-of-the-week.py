class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        days = 0
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

        for y in range(1971, year):
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                days += 366
            else:
                days += 365
                
        for m in range(month - 1):
            days += days_in_month[m]

        if month > 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            days += 1

        days += day - 1
        
        return week[days % 7]