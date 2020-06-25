class Solution:
    # adopted from
    # https://leetcode.com/problems/non-decreasing-array/discuss/106816/Python-Extremely-Easy-to-Understand
    def checkPossibility(self, nums: List[int]) -> bool:
        one, two = nums[:], nums[:]
        
        for i in range(1, len(one)):
            if one[i-1] > one[i]:
                one.pop(i-1)
                two.pop(i)
                break
        
        return one == sorted(one) or two == sorted(two)
    
    # https://leetcode.com/problems/non-decreasing-array/discuss/145699/EASY-Python-O(N)-beat-100
    def checkPossibility(self, nums: List[int]) -> bool:
        # An array of 2 numbers can always be fixed up
        if len(nums) <= 2:
            return True

        count = 0
        idx = -1
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                if count:
                    # Only one outlier allowed
                    return False
                else:
                    count += 1
                    idx = i

        if not count:
            return True

        # If idx == 0, nums[0] can be dropped to fix the sequence
        # If idx == len(nums)-2, nums[len(nums)-1] can be dropped to fix the sequence
        if idx == 0 or idx == len(nums)-2:
            return True

        # Check if nums[idx] can be dropped to fix the sequence
        if nums[idx+1] >= nums[idx-1]:
            return True
        # Check if nums[idx+1] can be dropped to fix the sequence
        if nums[idx+2] >= nums[idx]:
            return True
        
        # No way to fix the sequence
        return False
    
    # easier solution
    # https://leetcode.com/problems/non-decreasing-array/discuss/106842/The-easiest-python-solution....
    def checkPossibility(self, nums: List[int]) -> bool:
        canMod = 1
        for i, n in enumerate(nums[1:], 1):
            if nums[i - 1] > n: # we need to fix an inversion, either nums[i - 1] or nums[i], prefer nums[i - 1]
                if not canMod:
                    return 0
                if i > 1 and n < nums[i - 2]: # [3, 5, 2] no choice but to modify myself, otherwise greedily "fix" nums[i - 1]
                    nums[i] = nums[i - 1]
                canMod = 0
        return 1