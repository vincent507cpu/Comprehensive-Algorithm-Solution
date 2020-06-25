class Solution:
    # my solution
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lst = []
        
        for idx, row in enumerate(mat):
            i, num = 0, 0
            # print(i, row[i])
            while i < len(row) and row[i] == 1:
                num += 1
                i += 1
            lst.append((num, idx))
            
        return [row[1] for row in sorted(lst)[:k]]
    
    # shorter solution
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        S = [[sum(g),i] for i,g in enumerate(mat)]
        
        return [r[1] for r in sorted(R[:k])]