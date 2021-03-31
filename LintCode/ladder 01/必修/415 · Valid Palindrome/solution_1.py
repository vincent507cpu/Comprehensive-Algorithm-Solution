# cheating

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        if not s: return True

        res = ''

        for l in s:
            if l.isalpha() or l.isdigit():
                res += l.lower()

        return res == res[::-1]