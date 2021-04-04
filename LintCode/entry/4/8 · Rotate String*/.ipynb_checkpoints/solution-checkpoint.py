class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if not s or offset == 0:
            return s
        
        offset %= len(s)
        s[:-offset] = s[:-offset][::-1]
        s[-offset:] = s[-offset:][::-1]
        s[:] = s[:][::-1]