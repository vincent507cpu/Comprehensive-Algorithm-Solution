class Solution:
    """
    @param arr:  an array of non-negative integers
    @return: minimum number of elements
    """
    def minElements(self, arr):
        # write your code here
        arr.sort()
        
        res = 0
        total_old, total_new = sum(arr), 0
        
        while total_old > total_new:
            res += 1
            last = arr.pop()
            total_old -= last
            total_new += last
            
        return res