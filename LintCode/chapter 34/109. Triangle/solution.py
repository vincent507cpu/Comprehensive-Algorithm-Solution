# memoization search

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        return self.devide_conquer(triangle, 0, 0, {})

    def devide_conquer(self, triangle, x, y, memory):
        if x == len(triangle):
            return 0
            
        if (x, y) in memory:
            return memory[(x, y)]
            
        left = self.devide_conquer(triangle, x + 1, y, memory)
        right = self.devide_conquer(triangle, x + 1, y + 1, memory)
        
        memory[(x, y)] = min(left, right) + triangle[x][y]
        
        return memory[(x, y)]