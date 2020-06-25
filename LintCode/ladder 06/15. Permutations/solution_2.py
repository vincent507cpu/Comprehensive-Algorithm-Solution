# non-recursion way

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        nums.sort()
        result = []


        hasNext = True  # hasNext 为 true 时，表示可以继续迭代
        while hasNext:
            current = list(nums)  # 进行数组复制
            result.append(current)
            hasNext = self.nextPermutation(nums)
        
        return result


    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return
        
        i = n - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1


        if i <= 0:
            return False


        j = n-1
        while nums[j] <= nums[i-1]:
            j -= 1
        nums[j], nums[i-1] = nums[i-1], nums[j]
        
        self.swapList(nums, i, n-1)


        return True