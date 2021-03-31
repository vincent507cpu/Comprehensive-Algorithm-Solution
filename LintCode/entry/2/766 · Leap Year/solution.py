class Solution:
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """
    def isLeapYear(self, n):
        # write your code here
        if n % 400 == 0:
            return True

        if n % 4:
            return False
        elif n % 100 == 0:
            return False

        return True