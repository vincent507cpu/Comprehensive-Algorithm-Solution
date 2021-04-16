class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        if not dividend:
            return 0
        MAX_INT = 2147483647

        neg = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        index = 1
        while index * divisor <= dividend:
            index *= 2

        left, right = 0, index
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * divisor < dividend:
                left  = mid
            else:
                right = mid

        if right * divisor <= dividend:
            res = -right if neg else right
        elif left * divisor <= dividend:
            res = -left if neg else left

        if res > MAX_INT:
            return MAX_INT
        return res