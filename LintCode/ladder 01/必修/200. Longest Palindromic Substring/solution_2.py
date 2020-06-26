# two pointers

class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return s
            
        answer = (0, 0)
        for mid in range(len(s)):
            answer = max(answer, self.find_palindrome(s, mid, mid))
            answer = max(answer, self.find_palindrome(s, mid, mid + 1))
            
        return s[answer[1]: answer[0] + answer[1]]
        
    def find_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return right - left - 1, left + 1