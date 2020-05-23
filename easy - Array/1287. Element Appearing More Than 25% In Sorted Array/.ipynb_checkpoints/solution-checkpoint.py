class Solution:
    # my first solution
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        
        if length < 4:
            return arr[0]
        
        cnt = 1
        
        for i, n in enumerate(arr[1:], 1):
            if n != arr[i-1]:
                cnt = 1
            else:
                cnt += 1
                if cnt > length * 0.25:
                    return n
                
    # my second solution
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) < 4:
            return arr[0]
        
        threshold = len(arr) * 0.25
        dct = {}
        
        for n in arr:
            dct[n] = dct.get(n, 0) + 1
            if dct[n] > threshold:
                return n