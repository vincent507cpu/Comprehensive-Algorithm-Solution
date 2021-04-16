class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def stringCount(self, str):
        # Write your code here.
        left, right, res = 0, 0, 0

        while right < len(str):
            if str[right] == '0':
                right += 1
                res += right - left
            else:
                right += 1
                left = right

        return res