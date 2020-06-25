class Solution:
    # any dominoes count as loon as one pair is equivalent to another pair:
    # input: [[1,2],[1,2],[1,1],[1,2],[2,2]]
    # output: 3
    
    # my solution
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        seen = {}
        
        for pair in dominoes:
            pair = tuple(sorted(pair))
            seen[pair] = seen.get(pair, 0) + 1
        
        return sum([n * (n - 1) // 2 for n in seen.values()])