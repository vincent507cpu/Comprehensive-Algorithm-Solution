class Solution:
    def longestPalindrome(self, s: str) -> int:
        dct ={}
        
        for l in s:
            dct[l] = dct.get(l, 0) + 1
            
        even = [val for val in dct.values() if val % 2 == 0]
        odd = [val for val in dct.values() if val % 2 == 1]
        
        if odd and even:
            return sum(even) + sum(odd) - len(odd) + 1 
            # in case there are multiple letters with odd appearances, 
            # we need to substract 1 for each except the longest one
        elif even:
            return sum(even)
        elif odd:
            return max(odd) - len(odd) + 1
        
    # more concise solution
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
            
        letters = set(s)
        
        even = sum([s.count(x) for x in letters if s.count(x) % 2 == 0])
        odd = [s.count(x) for x in letters if s.count(x) % 2 == 1]
        
        return even + sum(odd) - len(odd) + 1 if odd else even
        
    ##################################################
    # Counter() solution.
    # Personally I try to use only built-in functions.
    # https://leetcode.com/problems/longest-palindrome/discuss/523664/python-counter-solution
    
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        res = 0
        for char in counter:
            res += counter[char] // 2 * 2
        return res if res == len(s) else res + 1