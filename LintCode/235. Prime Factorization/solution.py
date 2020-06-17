class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        result = []
        up = int(math.sqrt(num));
        
        k = 2
        while k <= up and num > 1: 
            while num % k == 0:
                num //= k
                result.append(k)
            k += 1
                
        if num > 1:
            result.append(num)
            
        return result