# https://leetcode.com/problems/sort-array-by-parity-ii/discuss/205903/Python-one-pass-O(1)-memory-simple-code-beats-90

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j = 0, 1
        
        while i < len(A) and j < len(A):
            if A[i] % 2 == 0:
                i += 2
                continue
                
            if A[j] % 2 == 1:
                j += 2
                continue
                
            if i < len(A) and j < len(A):
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
            
        return A