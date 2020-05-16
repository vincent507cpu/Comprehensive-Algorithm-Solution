# https://leetcode.com/problems/can-place-flowers/discuss/103890/Python-Straightforward-with-Explanation

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new  = [0] + flowerbed + [0]
        res = 0
        
        for i in range(1, len(new)-1):
            if new[i-1:i+2] == [0, 0, 0]:
                res += 1
                new[i] = 1
                
        return res >= n