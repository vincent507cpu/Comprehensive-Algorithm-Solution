class Solution:
    """
    @param s: a string
    @return: a string
    """
    def largestLetter(self, s):
        # write your code here
        s = set(s)
        res = set()

        for l in s:
            if l.isupper() and l.lower() in s:
                res.add(l)

        return max(res) if res else 'NO'