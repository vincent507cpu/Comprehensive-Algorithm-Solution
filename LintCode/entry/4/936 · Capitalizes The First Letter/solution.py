class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizesFirst(self, s):
        # Write your code here
        prev_letter = False
        res = []

        for i in range(len(s)):
            if not s[i].isalpha():
                res.append(s[i])
                prev_letter = False
            elif s[i].isalpha() and prev_letter:
                res.append(s[i])
            elif s[i].isalpha() and not prev_letter:
                res.append(s[i].upper())
                prev_letter = True

        return ''.join(res)