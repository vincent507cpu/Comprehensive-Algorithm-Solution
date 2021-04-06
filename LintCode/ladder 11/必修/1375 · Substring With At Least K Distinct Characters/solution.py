class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        if not s:
            return 0

        unique, res, dct = 0, 0, {}
        right = 0

        for i in range(len(s)):
            while right < len(s) and unique < k:
                dct[s[right]] = dct.get(s[right], 0) + 1

                if dct[s[right]] == 1:
                    unique += 1
                
                right += 1

            if unique == k:
                res += len(s) - right + 1
            
            dct[s[i]] -= 1

            if dct[s[i]] == 0:
                unique -= 1

        return res