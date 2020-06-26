class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        
        for _ in range(2, N + 1):
            a, b = b, a + b
            
        if N == 0:
            return a
        else: 
            return b