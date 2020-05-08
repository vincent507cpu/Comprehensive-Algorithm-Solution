class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # my solution, not so good. O(n2) time complexity, O(n) space complexity
        dct = {}
        res = []
        
        for word in A:
            tmp = set(word)
            for char in tmp:
                dct[char] = dct.get(char, []) + [word.count(char)]
                
        for key, val in dct.items():
            if len(val) == len(A):
                for _ in range(min(val)):
                    res.append(key)
                    
        return res
    
    def commonChars(self, A: List[str]) -> List[str]:
        # better solution: O(n2) time complexity, O(1) space complexity
        # adopted from https://leetcode.com/problems/find-common-characters/discuss/247558/JavaPython-3-12-liner-and-7-liner-count-and-look-for-minimum.
        cnt = [100*100+1] * 26
        
        for s in A:
            cnt2 = [0] * 26
            for c in s:
                cnt2[ord(c) - ord('a')] += 1
            cnt = [min(cnt[i], cnt2[i]) for i in range(26)]   

        res = []
        
        for i in range(26):
            for _ in range(cnt[i]):
                res.append(chr(ord('a')+i))
                
        return res