class Solution:
    # my solution
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res, diff = [], float('inf')
        
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] < diff:
                diff = arr[i+1] - arr[i]
                res = [[arr[i], arr[i+1]]]
            elif arr[i+1] - arr[i] == diff:
                res.append([arr[i], arr[i+1]])
                
        return res
    
    # zip
    # https://leetcode.com/problems/minimum-absolute-difference/discuss/387580/Python3-3-liner
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn] 