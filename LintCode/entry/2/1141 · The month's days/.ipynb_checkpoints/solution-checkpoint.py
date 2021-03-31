class Solution:
    """
    @param year: a number year
    @param month: a number month
    @return: Given the year and the month, return the number of days of the month.
    """
    def getTheMonthDays(self, year, month):
        # write your code here
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if month in [4, 6, 9, 11]:
            return 30
            
        if month == 2 and not year % 4 and year % 100:
            return 29
        else:
            return 28