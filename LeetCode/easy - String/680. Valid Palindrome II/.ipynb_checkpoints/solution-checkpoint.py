class Solution:
    # two pointers
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        left, right = self.findDifference(s, 0, len(s)-1)
        if left >= right:
            return True
        
        return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)
        
    def isPalindrome(self, s, left, right):
        left, right = self.findDifference(s, left, right)
        return left >= right
        
    def findDifference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right
    
    '''
    We can use the standard two-pointer approach that starts at the left and right of the string and move inwards. Whenever there is a mismatch, we can either exclude the character at the left or the right pointer. We then take the two remaining substrings and compare against its reversed and see if either one is a palindrome.
    '''
    # https://leetcode.com/problems/valid-palindrome-ii/discuss/107718/Easy-to-Understand-Python-Solution
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                one, two = s[l:r], s[l+1:r+1]
                return one == one[::-1] or two == two[::-1]
            l += 1
            r -= 1
        return True
    
    # recursion
    def validPalindrome(self, s: str) -> bool:
        return self.verify(s, 0, len(s) - 1, False)
    
    def verify(self, s, l, r, deleted):
        while l < r:
            if s[l] != s[r]:
                if deleted == True:
                    return False
                else:
                    return self.verify(s, l+1, r, True) or self.verify(s, l, r-1, True)
            else:
                l += 1
                r -= 1
        
        return True