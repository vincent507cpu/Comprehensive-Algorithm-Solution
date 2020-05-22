# my solution
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        new = []
        
        for j in range(len(A[0])):
            tmp = []
            for i in range(len(A)):
                tmp.append(A[i][j])
            new.append(tmp)
                
        return new