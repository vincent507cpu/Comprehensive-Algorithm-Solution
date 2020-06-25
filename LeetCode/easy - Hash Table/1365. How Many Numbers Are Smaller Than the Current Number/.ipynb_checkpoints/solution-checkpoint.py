class Solution:
    # my initial solution, n(O2) time complexity, took 668 ms in 5 test
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dct = {}
        lst = []
        
        for n in nums:
            dct[n] = dct.get(n, 0) + 1
            
        print(dct)
        for n in nums:
            res = sum([val for key, val in dct.items() if key < n])
            lst.append(res)
            
        return lst
    
    # better solution, n(O) time complexity, took 244 ms in 5 tests
    # https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/discuss/524865/Clean-Python-3-sorting-and-counting
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dct = {}
        for i, n in enumerate(sorted(nums)):
            if n not in dct:
                dct[n] = i
        return [dct[n] for n in nums]