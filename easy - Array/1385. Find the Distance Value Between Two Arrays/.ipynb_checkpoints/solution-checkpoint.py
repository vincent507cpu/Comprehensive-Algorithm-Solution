class Solution:
    # my solution, brute force
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        
        for m in arr1:
            flag = False
            for n in arr2:
                if abs(m - n) <= d:
                    flag = True
                    
            if not flag:
                res += 1
                    
        return res
    
    # hash & search coverage
    # https://leetcode.com/problems/find-the-distance-value-between-two-arrays/discuss/640002/Python-Short-and-Simple
    class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1, arr2 = collections.Counter(arr1), set(arr2)
        
        res = 0
        for num in arr1:
            target = range(num - d, num + d + 1)
            if not arr2.intersection(target):
                res += arr1[num]
        
        return res