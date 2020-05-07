# my solution
# https://leetcode.com/problems/shortest-completing-word/discuss/617579/intuitive-solution-faster-than-96

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words.sort(key=len)
        licensePlate = licensePlate.lower()
        
        for w in words:
            flag = True
            for char in licensePlate:
                if char.isalpha():
                    if char not in w or licensePlate.count(char) > w.count(char):
                        flag = False
                        
            if flag == True:
                return w