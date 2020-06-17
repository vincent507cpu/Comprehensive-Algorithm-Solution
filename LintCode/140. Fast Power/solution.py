class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    # recursion
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
            
        product = self.fastPower(a, b, n // 2)
        product = (product * product) % b
        
        if n % 2 == 1:
            product = (product * a) % b
            
        return product
    
    # non-recursion
    def fastPower(self, a, b, n):
        # write your code here
        ans = 1
        
        while n > 0:
            if n % 2 == 1:
                ans = (ans * a) % b
                
            a = a * a % b
            n = n // 2
            
        return ans % b