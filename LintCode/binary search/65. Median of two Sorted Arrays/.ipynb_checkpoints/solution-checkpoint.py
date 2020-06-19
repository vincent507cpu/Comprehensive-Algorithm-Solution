class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    # two ponters, O(m+n)
    def findMedianSortedArrays(self, A, B):
        # write your code here
        m, n = len(A), len(B)
        p1, p2 = 0, 0
        left, right = 0, 0
        
        for i in range((m + n) // 2 + 1):
            left = right
            
            if p1 >= m or p2 < n and A[p1] > B[p2]:
                right = B[p2]
                p2 += 1
            else:
                right = A[p1]
                p1 += 1
                
        if (m + n) % 2 == 1:
            return right
        else:
            return (left + right) / 2
        
    # devide and conquer
    class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        n = len(A) + len(B)
        
        if n % 2 == 1:
            return self.findKth(A, 0, B, 0, n // 2 + 1)
        else:
            small = self.findKth(A, 0, B, 0, n // 2)
            big = self.findKth(A, 0, B, 0, n // 2 + 1)
            return (small + big) / 2
            
    def findKth(self, A, index_a, B, index_b, k):
        if len(A) == index_a:
            return B[index_b + k - 1]
            
        if len(B) == index_b:
            return A[index_a + k - 1]
            
        if k == 1:
            return min(A[index_a], B[index_b])
            
        a = A[index_a + k // 2 - 1] if index_a + k // 2 <= len(A) else None
        b = B[index_b + k // 2 - 1] if index_b + k // 2 <= len(B) else None
        
        if not b or (a and a < b):
            return self.findKth(A, index_a + k // 2, B, index_b, k - k // 2)
        return self.findKth(A, index_a, B, index_b + k // 2, k - k // 2)