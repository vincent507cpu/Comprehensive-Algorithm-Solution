class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    
    # algorithm 1: Python set
    def intersection(self, nums1, nums2):
        # write your code here
        return list(set(nums1).intersection(set(nums2)))
    
    # algorithm 2: two pointers
    def intersection(self, nums1, nums2):
        # write your code here
        nums1.sort()
        nums2.sort()
        
        i, j = 0, 0
        last_num, res = float('inf'), []
        
        while i < len(nums1) and j < len(nums2):
            if i < len(nums1) and j < len(nums2) and nums1[i] < nums2[j]:
                i += 1
            elif i < len(nums1) and j < len(nums2) and nums1[i] > nums2[j]:
                j += 1
            else:
                if i < len(nums1) and j < len(nums2) and nums1[i] == last_num:
                    i += 1
                    j += 1
                    continue
                res.append(nums1[i])
                last_num = nums1[i]
                i += 1
                j += 1

        return res
    
    #algorithm 3: binary search
    def intersection(self, nums1, nums2):
        # write your code here
        nums1.sort()
        nums2.sort()

        if len(nums2) > len(nums1):
            return self.binary_search(nums2, nums1)
        else:
            return self.binary_search(nums1, nums2)
        
        
    def binary_search(self, being_compared, compare):
        res = []
        last_num = float('inf')
        for target in compare:
            start, end = 0, len(being_compared) - 1
            while start + 1 < end:
                mid = (start + end) // 2
                if being_compared[mid] < target:
                    start = mid
                elif being_compared[mid] >= target:
                    end = mid
            if being_compared[start] == target and last_num != being_compared[start]:
                res.append(being_compared[start])
                last_num = being_compared[start]
            if being_compared[end] == target and last_num != being_compared[end]:
                res.append(being_compared[end])
                last_num = being_compared[end]

        return res