class Solution:
    '''
    2 scenarios:
    1) the maximum is the product of three positive integers;
    2) the maximum is the product of two negative integers and one positive integer;
    
    We just need to calculate these two products and compare them.
    '''
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        cond1 = nums[0] * nums[1] * nums[-1]
        cond2 = nums[-3] * nums[-2] * nums[-1]

        return max(cond1, cond2)