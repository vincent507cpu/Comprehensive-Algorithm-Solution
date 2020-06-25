class Solution:
    # my solution
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        start, end, tmp = 0, 0, 1
        
        for i, n in enumerate(S[1:], 1):
            if S[i-1] == n:
                tmp += 1
                end = i
            elif tmp > 2 and S[i-1] != n:
                res.append([start, end])
                start = i
                tmp = 1
            else:
                start = i
                tmp = 1

        res.append([start, end]) if tmp > 2 else None
        return res