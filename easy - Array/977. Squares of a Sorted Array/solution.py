class Solution:
    # cheating
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x**2 for x in A])
    
    # deque
    # https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100
    def sortedSquares(self, A: List[int]) -> List[int]:
        from collections import deque
        res = deque()
        
        l, r = 0, len(A) - 1
        
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            
            if left < right:
                res.appendleft(right * right)
                r -= 1
            else:
                res.appendleft(left * left)
                l += 1
                
        return res
    
    # list
    # https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        l, r = 0, len(A) - 1
        
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left <= right:
                res[r-l] = right * right
                r -= 1
            else:
                res[r-l] = left * left
                l += 1
                
        return res