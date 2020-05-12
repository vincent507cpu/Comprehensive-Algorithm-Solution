# consulted 
# https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for _ in range(2, numRows+1):
            tmp1 = [0] + res[-1]
            tmp2 = res[-1] + [0]
            
            new = [x + y for x, y in zip(tmp1, tmp2)]
            res.append(new)
            
        return res if numRows else []