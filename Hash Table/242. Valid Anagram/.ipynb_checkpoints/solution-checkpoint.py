class Solution:
    # https://leetcode.com/problems/valid-anagram/discuss/255473/Easy-Code-for-Valid-Anagram
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(list(t))==sorted(list(s)):
            return True
        else:
            return False
    
    # use collections.Counter
    # https://leetcode.com/problems/valid-anagram/discuss/551486/Python-3-%22one%22-line-solution-faster-than-100
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        
        return Counter(s) == Counter(t)
    
    # follow up: What if the inputs contain unicode characters? How would you adapt your solution to such case?
    # https://leetcode.com/problems/valid-anagram/discuss/66747/My-Python-submission.-Better-than-up-to-98.
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [chr(ord('a')+i) for i in range(26)]
        countS = [s.count(char) for char in alpha]
        countT = [t.count(char) for char in alpha]
        for (x,y) in zip(countS,countT):
            if x != y:
                return False
        return True