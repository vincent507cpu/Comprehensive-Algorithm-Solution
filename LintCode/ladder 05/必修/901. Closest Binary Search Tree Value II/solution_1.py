"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 先遍历整个二叉树，获得一个数组，然后找到比 target 小的最大值，然后背向双指针

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        if not root or k == 0:
            return []
            
        nums = self.get_inorder(root)
        left = self.find_lower_index(nums, target)
        right = left + 1
        res = []
        for _ in range(k):
            if self.is_left_closer(nums, left, right, target):
                res.append(nums[left])
                left -= 1
            else:
                res.append(nums[right])
                right += 1
                
        return res
        
    def get_inorder(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        inorder = []
        
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)
                
        return inorder
        
    def find_lower_index(self, nums, target):
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[end] < target:
            return end
        if nums[start] < target:
            return start
        return -1
            
    def is_left_closer(self, nums, left, right, target):
        if left < 0:
            return False
        if right >= len(nums):
            return True
        return target - nums[left] < nums[right] - target
