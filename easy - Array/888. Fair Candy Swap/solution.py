# https://leetcode.com/problems/fair-candy-swap/discuss/161269/C%2B%2BJavaPython-Straight-Forward

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B)) // 2
        
        for b in set(B):
            if b + diff in A:
                return [b+diff, b]