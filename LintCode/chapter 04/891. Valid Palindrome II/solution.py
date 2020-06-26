class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        l, r = self.findDifference(s, 0, len(s) - 1)
        if l >= r:
            return True
        return self.isPalindrome(s, l+1, r) or self.isPalindrome(s, l, r-1)
        
    def isPalindrome(self, s, l, r):
        l, r = self.findDifference(s, l, r)
        return l >= r
        
    def findDifference(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return l, r
            l += 1
            r -= 1
        return l, r