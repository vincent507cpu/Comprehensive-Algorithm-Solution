# O(k) space complexity

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        
        for _ in range(rowIndex):
            res = [x + y for (x, y) in zip(res+[0], [0]+res)]
            
        return res