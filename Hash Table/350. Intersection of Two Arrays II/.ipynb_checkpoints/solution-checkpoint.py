# base model, ugly

class Solution:
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        lst = []

        for i in range(len(nums1)):
            if nums2 and nums1[i] in nums2:
                lst.append(nums1[i])
                idx = nums2.index(nums1[i])
                nums2.pop(idx)
                
        return lst
    
    ###################################################
    # sorted lists:
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        lst = []
#         nums1.sort()
#         nums2.sort()
        
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                lst.append(nums1[i])
                i += 1
                j += 1
                
        return lst
    
    ###################################################
    # use dictionary
    def intersect3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        lst = []
        dct = {}
        
        for num in nums2:
            dct[num] = dct.get(num, 0) + 1
            
        for num in nums1:
            if num in dct and dct[num] > 0:
                lst.append(num)
                dct[num] -= 1
                
        return lst