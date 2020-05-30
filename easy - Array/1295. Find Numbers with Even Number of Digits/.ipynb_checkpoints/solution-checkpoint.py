class Solution:
    # my solution
    def findNumbers(self, nums: List[int]) -> int:
        return sum([len(str(d)) % 2 == 0 for d in nums])