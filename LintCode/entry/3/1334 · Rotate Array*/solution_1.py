class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums, k):
        # Write your code here
        k %= len(nums)
        
        return nums[-k:] + nums[:-k]