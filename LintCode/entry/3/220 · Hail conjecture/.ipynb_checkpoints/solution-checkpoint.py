class Solution:
    """
    @param num: an integer
    @return: return an integer
    """
    def getAnswer(self, num):
        # write your code here.
        res = 0

        while num != 1:

            if not num % 2:
                num /= 2
            else:
                num = num * 3 + 1

            res += 1
        
        return res