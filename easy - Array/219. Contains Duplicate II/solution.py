class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    # my sotluion
        dct = {}
        
        for i, num in enumerate(nums):
            dct[num] = dct.get(num, []) + [i]
            
        keys = [key for key, val in dct.items() if len(val) > 1]
        
        if keys:
            for key in keys:
                if min([i - j for i in dct[key] for j in dct[key] if i - j > 0]) <= k:
                    return True
            
        return False
        
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    # better solution
        dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False