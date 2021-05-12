class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if not nums:
            return [[]]

        nums.sort()
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, idx, subset, res):
        res.append(subset[:])

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue

            subset.append(nums[i])
            self.dfs(nums, i+1, subset, res)
            subset.pop()