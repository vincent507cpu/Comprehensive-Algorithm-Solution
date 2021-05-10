class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        res[0][0] = 1
        DIR = {(0, 1):(1, 0), (1, 0):(0, -1), (0, -1):(-1, 0), (-1, 0):(0, 1)}
        move = (0, 1)
        x, y = 0, 0
        val, step = 2, 1
        
        while step < n * n:
            if 0 <= x + move[0] < n and 0 <= y + move[1] < n \
                and res[x + move[0]][y + move[1]] == 0:
                res[x + move[0]][y + move[1]] = val
                val += 1
                step += 1
                x += move[0]
                y += move[1]
            else:
                move = DIR[move]
        
        return res