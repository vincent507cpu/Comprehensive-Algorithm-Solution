class Solution:
    # my first solution: iteration, low efficiency
    def findLucky(self, arr: List[int]) -> int:
        dct, res = {}, []
        
        for n in arr:
            dct[n] = dct.get(n, 0) + 1
            
        for key, val in dct.items():
            if key == val:
                res.append(key)
                
        if res:
            return max(res)
        else:
            return -1
        
    # my second solution: collections.Counter, more efficient
    def findLucky(self, arr: List[int]) -> int:
        res = 0
        
        counter = collections.Counter(arr)
        
        for key, val in counter.items():
            if key == val:
                res = max(res, key)
                
        return res if res else -1
    
    # fill a new array
    # https://leetcode.com/problems/find-lucky-integer-in-an-array/discuss/554838/JavaPython-3-Two-clean-codes%3A-array-and-HashMapCounter.
    def findLucky(self, arr: List[int]) -> int:
        res = [0] * 501
        
        for n in arr:
            res[n] += 1
            
        for i in range(500, 0, -1):
            if i == res[i]:
                return i
            
        return -1