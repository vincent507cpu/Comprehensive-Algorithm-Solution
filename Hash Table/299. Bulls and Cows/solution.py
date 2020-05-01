# best solution
# https://leetcode.com/problems/bulls-and-cows/discuss/74616/3-lines-in-Python

class Solution:
    def getHint(self, secret, guess):
        from operator import eq
        
        bulls = sum(map(eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return f'{bulls}A{both - bulls}B'