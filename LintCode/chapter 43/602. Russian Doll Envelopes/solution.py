class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        lst = [float('inf')] * (len(envelopes) + 1)
        lst[0] = float('-inf')
        
        res = 0
        for _, h in envelopes:
            index = self.first_gte(lst, h)
            lst[index] = h
            res = max(res, index)
        
        return res
        
    def first_gte(self, lst, val):
        start, end = 0, len(lst) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if lst[mid] >= val:
                end = mid
            else:
                start = mid
        
        if lst[start] >= val:
            return start
        return end