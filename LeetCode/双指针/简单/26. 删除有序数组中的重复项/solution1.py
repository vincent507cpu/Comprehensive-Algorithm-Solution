# 如果数组 nums 的长度为 0，则数组不包含任何元素，因此返回 0。
# 当数组 nums 的长度大于 0 时，数组中至少包含一个元素，在删除重复元素之后也至少剩下一个元素，因此 nums[0] 保持原状即可，从下标 1 开始删除重复元素。
# 定义两个指针 fast 和 slow 分别为快指针和慢指针，快指针表示遍历数组到达的下标位置，慢指针表示下一个不同元素要填入的下标位置，初始时两个指针都指向下标 1。
# 将快指针 fast 从 1 遍历到 n-1，如果 nums[fast - 1] != nums[fast]，则 nums[fast] 与之前的数都不同，将 nums[fast] 复制到 nums[slow]，slow += 1。
# 遍历结束后返回 slow。

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        slow, fast = 1, 1
        while fast < len(nums):
            if nums[fast - 1] == nums[fast]:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1

        return slow