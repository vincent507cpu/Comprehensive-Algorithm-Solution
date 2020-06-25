class Solution:
    # use ditctionary
    def firstUniqChar(self, s: str) -> int:
        dct = {}
        
        for i, l in enumerate(s):
            dct[l] = dct.get(l, []) + [i]
            
        res = [val[0] for val in dct.values() if len(val) == 1]
        if res:
            return min(res)
        else:
            return -1
    
    ########################################################
    # use count methed
    # https://leetcode.com/problems/first-unique-character-in-a-string/discuss/519050/Easy-python-solution
    def firstUniqChar(self, s: str) -> int:
        for i, l in enumerate(s):
            if s.count(l) == 1:
                return i
            
        return -1
    
    ########################################################
    # construct a alphabatical lookup table
    # https://leetcode.com/problems/first-unique-character-in-a-string/discuss/473340/Simplest-solution
    def firstUniqChar(self, s: str) -> int:
        arr = [0 for i in range(26)]
        
        for i in range(len(s)):
            arr[ord(s[i])-97]+=1
            
        for j in range(len(s)):
            if(arr[ord(s[j])-97] == 1):
                return j
        return -1