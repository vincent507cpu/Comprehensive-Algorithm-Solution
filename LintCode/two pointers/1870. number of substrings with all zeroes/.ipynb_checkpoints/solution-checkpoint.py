class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    # two pointers
    def stringCount(self, str):
        # Write your code here.
        res, j = 0, 1
        
        for i in range(len(str)):
            if str[i] == '1':
                continue
            j = max(j, i + 1)
            while j < len(str) and str[j] == '0':
                j += 1
            res += j - i

        return res