# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/discuss/441452/Python3-Reasonably-concise-solution
'''
For each player, we use a list score of 8 elements with below meaning
0-2 : number of characters placed at each row
3-5 : number of characters placed at each column
6 : number of characters placed at diagonal
7 : number of characters placed at anti-diagonal
to keep track of his/her winning status.

Here, "A" and "B" correspond to the two rows of score.
'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        score = [[0]*8 for _ in range(2)]
        
        p = 0 #start with player A
        for i, j in moves:
            score[p][i] += 1
            score[p][3+j] += 1
            score[p][6] += (i == j)
            score[p][7] += (i+j == 2)
            if any(x == 3 for x in score[p]): return ["A", "B"][p]
            p ^= 1 #switch player
            
        return "Pending" if len(moves) < 9 else "Draw"