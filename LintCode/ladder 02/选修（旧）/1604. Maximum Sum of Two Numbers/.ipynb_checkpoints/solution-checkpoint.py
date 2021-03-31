class Solution:
    """
    @param A: An Integer array
    @return: returns the maximum sum of two numbers
    """
    def MaximumSum(self, A):
        # write your code here
        result = -1
        dct = {}
        
        for num in A:
            tmp = self.digit_sum(num)
            dct[tmp] = dct.get(tmp, []) + [num]
            
            if len(dct[tmp]) > 1:
                dct[tmp].sort()
                result = max(result, dct[tmp][-1] + dct[tmp][-2])
                
        return result
        
    def digit_sum(self, num):
        res = 0
        
        while num // 10:
            res += num % 10
            num //= 10
        
        return res + num