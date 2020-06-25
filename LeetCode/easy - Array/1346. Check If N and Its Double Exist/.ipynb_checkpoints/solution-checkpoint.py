class Solution:
    # my ugly solution
    def checkIfExist(self, arr: List[int]) -> bool:
        neg = sorted([x for x in arr if x < 0], reverse=True)
        pos = sorted([x for x in arr if x >= 0])
        
        new = neg + pos
        for i, num in enumerate(new):
            j = i + 1
            if j < len(new) and new[j] < 0:
                while j < len(new) and new[j] >= num * 2:
                    if new[j] == num * 2:
                        return True
                    j += 1
            else:
                while j < len(new) and new[j] <= num * 2:
                    if new[j] == num * 2:
                        return True
                    j += 1
                
        return False
    
    # better but slower solution
    # https://leetcode.com/problems/check-if-n-and-its-double-exist/discuss/503657/1-line-Python
    def checkIfExist(self, arr: List[int]) -> bool:
        return arr.count(0) > 1 or any([x * 2 in arr for x in arr if x])
    
    # fastest solution: hash
    # https://leetcode.com/problems/check-if-n-and-its-double-exist/discuss/503441/JavaPython-3-HashSet-w-analysis.
    def checkIfExist(self, arr: List[int]) -> bool:
        res = set()
        
        for n in arr:
            if n * 2 in res or (n // 2 in res and n % 2 == 0):
                return True
            res.add(n)
            
        return False
    
    # not bad solution
    # https://leetcode.com/problems/check-if-n-and-its-double-exist/discuss/503714/Python3-Counter-O(n)-100
    def checkIfExist(self, arr: List[int]) -> bool:
        res = collections.Counter(arr)
        
        if res[0] > 1:
            return True
        
        for n in res:
            if res[n * 2] and n != 0:
                return True

        return False