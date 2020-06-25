class Solution:
    def thirdMax(self, nums: List[int]) -> int:
    # my initial solution, not quite get there b/c time is O(nlogn)
        nums = sorted(list(set(nums)))
        
        try:
            return nums[-3]
        except:
            return nums[-1]
        
    # https://leetcode.com/problems/third-maximum-number/discuss/90207/Intuitive-and-Short-Python-solution
    def thirdMax(self, nums: List[int]) -> int:
        lst = [-float('inf'), -float('inf'), -float('inf')]
        
        for n in nums:
            if n not in lst:
                if n > lst[0]:
                    lst = [n, lst[0], lst[1]]
                elif n > lst[1]:
                    lst = [lst[0], n, lst[1]]
                elif n > lst[2]:
                    lst = [lst[0], lst[1], n]
                    
        return lst[0] if -float('inf') in lst else lst[2]