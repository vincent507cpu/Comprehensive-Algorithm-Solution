# best solution
# https://leetcode.com/problems/bulls-and-cows/discuss/74616/3-lines-in-Python

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bull += 1
                
        total = sum(min(secret.count(n), guess.count(n)) for n in set(guess))
            
        return f'{bull}A{total-bull}B'