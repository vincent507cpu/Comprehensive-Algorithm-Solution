class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + 1 if digits[i] != 9 else 0
            if digits[i]:
                return digits
        digits.insert(0, 1)
        return digits