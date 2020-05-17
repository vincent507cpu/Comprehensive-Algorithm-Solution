# https://leetcode.com/problems/maximum-average-subarray-i/discuss/105435/2-lines-Python-2-versions

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = [0] + nums
        for i in range(len(sum)):
            sum[i] += sum[i-1]
            
        return max(sum[i+k]-sum[i] for i in range(len(sum)-k)) / k