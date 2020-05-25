class Solution:
    # my solution
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dct = {}
        
        for n in deck:
            dct[n] = dct.get(n, 0) + 1
            
        vals = dct.values()
        
        for i in range(2, min(vals) + 1):
            if sum([0 if val % i == 0 else 1 for val in vals]) == 0:
                return True
            
        return False