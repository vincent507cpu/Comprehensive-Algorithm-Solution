class Solution:
    # my solution
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        cur = -1
        
        while i >= 0:
            if arr[i] > cur:
                arr[i], cur = cur, arr[i]
            else:
                arr[i] = cur
            i -= 1
                
        
        return arr