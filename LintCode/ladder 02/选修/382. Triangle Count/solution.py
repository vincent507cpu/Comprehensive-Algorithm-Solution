class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        res = 0
        S.sort()
        
        for i in range(len(S) - 1, 1, -1):
            left, right = 0, i - 1

            while left < right:
                if S[left] + S[right] > S[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
                    
        return res