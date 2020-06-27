class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        if not self.distinct(s, k):
            return 0
            
        res = 0
        for i in range(len(s)):
            j = i + k
            while j <= len(s):
                if self.distinct(s[i:j], k):
                    res += len(s) - j + 1
                    break
                j += 1
                
        return res
            
    def distinct(self, chars, k):
        return len(set(list(chars))) >= k