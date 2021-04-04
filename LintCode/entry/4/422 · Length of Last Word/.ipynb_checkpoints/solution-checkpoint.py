class Solution:
    """
    @param s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        # write your code here
        if not s:
            return 0

        s = s.split()
        return len(s[-1])