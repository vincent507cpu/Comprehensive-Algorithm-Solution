class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution
        while n:
            if m and nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
                
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        nums1.sort()