class Solution:
    # two dictionaries
    def findTheDifference(self, s: str, t: str) -> str:
        dct = {}
        
        for l in t:
            dct[l] = dct.get(l, 0) + 1
            
        for l in s:
            dct[l] -= 1
            
        return [key for key, val in dct.items() if val == 1][0]
    
    ###################################################
    # convert to unicode
    # https://leetcode.com/problems/find-the-difference/discuss/86946/1-liners-Python-%2B-Ruby
    def findTheDifference(self, s, t):
        return chr(sum(map(ord, t)) - sum(map(ord, s)))