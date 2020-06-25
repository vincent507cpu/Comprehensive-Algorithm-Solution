class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    # my solution
        new = set(range(len(nums)+1))
        old = set(nums)
        return new.difference(old).pop()
    
    def missingNumber(self, nums: List[int]) -> int:
    # other solutions
    # https://leetcode.com/problems/missing-number/discuss/69832/1%2B-lines-Ruby-Python-Java-C%2B%2B
        n = len(nums)
        return n*(n+1)//2 - sum(nums)