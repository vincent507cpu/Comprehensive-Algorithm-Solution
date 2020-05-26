class Solution:
    # my solution
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        tmp = sum([x for x in A if x % 2 == 0])
        
        for query in queries:    
            A[query[1]] += query[0]
            
            if query[0] % 2 == 0 and A[query[1]] % 2 == 0:
                tmp += query[0]
            elif query[0] % 2 == 1 and A[query[1]] % 2 == 1:
                tmp -= (A[query[1]] - query[0])
            elif query[0] % 2 == 1 and A[query[1]] % 2 == 0:
                tmp += A[query[1]]
                
            res.append(tmp)
            
        return res
    
    # simpler solution
    # https://leetcode.com/problems/sum-of-even-numbers-after-queries/discuss/293545/Simple-Python3-Faster-Than-80
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        tmp = sum([x for x in A if x % 2 == 0])
        
        for val, idx in queries:
            if A[idx] % 2 == 0:
                tmp -= A[idx]
            
            A[idx] += val
            
            if A[idx] % 2 == 0:
                tmp += A[idx]
                
            res.append(tmp)
            
        return res