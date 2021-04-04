class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):
        # Write your code here
        i = 32
        res = []

        while n < 2 ** i - 1 and i > 0:
            i -= 1

        while i >= 0:
            if n >= 2 ** i:
                res.append(1)
                n -= 2 ** i
                i -= 1
            else:
                res.append(0)
                i -= 1

        return res == res[::-1]