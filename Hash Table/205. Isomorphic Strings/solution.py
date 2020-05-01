class Solution:
    def isIsomorphic1(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        
        dct = {}
        
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = t[i]
            elif dct[s[i]] != t[i]:
                return False
            
        return True
    
    # additional solutions:
    # https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-(dictionary-etc).
    def isIsomorphic2(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        
        for i in range(len(s)):
            d1[s[i]] = d1.get(s[i], []) + [i]
            d2[t[i]] = d2.get(t[i], []) + [i]
            
        return sorted(d1.values()) == sorted(d2.values())
    
    def isIsomorphic3(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))