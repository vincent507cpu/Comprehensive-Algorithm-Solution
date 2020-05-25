class Solution:
    # my solution
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start, end = 0, len(A) - 1
        
        while start < end:
            if A[start] % 2 == 1 and  A[end] % 2 == 0:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
            elif A[start] % 2 == 0:
                start += 1
            elif A[end] % 2 == 1:
                end -= 1
                
        return A
    
    # two simpler but slower solutions
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x % 2)
    
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if not x % 2] + [x for x in A if x % 2]