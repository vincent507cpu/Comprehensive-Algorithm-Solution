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
    
    # list reversal
    # https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        l, r = 0, len(A) - 1
        
        while l <= r:
            if A[l] <= A[r]:
                res.append(A[l] ** 2)
                r -= 1
            else:
                res.append(A[r] ** 2)
                l += 1
                
        return reversed(res)