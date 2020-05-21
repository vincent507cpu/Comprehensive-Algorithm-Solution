# https://leetcode.com/problems/maximum-average-subarray-i/discuss/105435/2-lines-Python-2-versions

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        new = [0] + nums
        for i in range(len(new)):
            new[i] += new[i-1]
            
        return max(new[i+k]-new[i] for i in range(len(new)-k)) / k