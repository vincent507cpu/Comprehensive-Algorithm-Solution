class Solution:
    # https://leetcode.com/problems/rank-transform-of-an-array/discuss/540140/Python-clean-code-hashmap
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dct, rank = {}, 1
        
        for n in sorted(set(arr)):
            dct[n] = rank
            rank += 1
            
        return [dct[x] for x in arr]
    
    # more concise solution
    # https://leetcode.com/problems/rank-transform-of-an-array/discuss/489753/C%2B%2BPython-HashMap
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dct = {}
        
        for n in sorted(set(arr)):
            dct[n] = dct.get(n, len(dct) + 1)
            
        return [dct[x] for x in arr]
    
    # more simpler solution
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tmp = sorted(set(arr))
        dct = {n:i+1 for i, n in enumerate(tmp)}

        return [dct[n] for n in arr]