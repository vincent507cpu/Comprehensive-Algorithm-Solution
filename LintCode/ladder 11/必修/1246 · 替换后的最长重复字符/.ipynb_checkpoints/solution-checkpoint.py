# https://blog.csdn.net/qq_17550379/article/details/99309142

class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        # write your code here
        if not s:
            return 0

        res, l, dct, freq = 0, 0, {}, 0

        for r, c in enumerate(s):
            dct[s[r]] = dct.get(s[r], 0) + 1
            freq = max(freq, dct[s[r]])

            while r - l + 1 - freq > k:
                dct[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res