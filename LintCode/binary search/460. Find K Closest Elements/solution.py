class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    # brutal force
    def kClosestNumbers(self, A, target, k):
        # write your code here
        res = []
        
        for n in A:
            res.append((abs(n - target), n))
            
        return [x[1] for x in sorted(res)[:k]]
    
    # two pointers + binary search
    def kClosestNumbers(self, A, target, k):
        # write your code here
        right = self.findRightClosest(A, target)
        left = right - 1
        
        res = []
        for _ in range(k):
            if self.isLeftCloser(A, target, left, right):
                res.append(A[left])
                left -= 1
            else:
                res.append(A[right])
                right += 1
                
        return res
        
    def findRightClosest(self, A, target):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] >= target:
                right = mid
            else:
                left = mid
                
        if A[left] >= target:
            return left
            
        if A[right] >= target:
            return right
            
        return len(A)
            
    def isLeftCloser(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
            
        return target - A[left] <= A[right] - target