class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def dropEggs(self, n):
        # write your code here
        x = int((n * 2) ** 0.5)
        
        while x * (x + 1) / 2 < n:
            x += 1
            
        return x