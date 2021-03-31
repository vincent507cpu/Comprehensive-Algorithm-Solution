# quick sort

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    '''
    令left = l，right = r，pivot = nums[left]。
    当nums[right] >= pivot时，right指针向左移动，交换left和right处的值。
    当nums[left] < pivot时，right指针向右移动，交换left和right处的值。
    直到两指针相遇，否则回到第2步。
    '''
    def kthLargestElement(self, n, nums):
        length = len(nums)
        # 为了方便编写代码，这里将第 n 大转换成第 n 小问题。
        n = length - n
        return self.partition(nums, 0, length - 1, n)
    
    def partition(self, nums, l, r, n):
        left, right = l, r
        pivot = nums[left]
        
        while left < right:
            while left < right and nums[left] <= nums[right]:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            while left < right and nums[left] <= nums[right]:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]
        
        nums[left] = pivot
        # 如果第 n 小在右侧，搜索右边的范围，否则搜索左侧。
        if left < n:
            return self.partition(nums, left + 1, r, n)
        if left > n:
            return self.partition(nums, l, right - 1, n)
        return nums[n]