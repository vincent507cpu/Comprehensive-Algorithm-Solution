"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        tmp = []
        
        for interval_lst in intervals:
            for interval in interval_lst:
                tmp.append(interval)
                
        tmp = sorted(tmp, key=lambda x: x.start)
        
        if not len(tmp):
            return []
        
        res = [tmp[0]]
        
        for i in range(1, len(tmp)):
            if res[-1].end >= tmp[i].start:
                res[-1].end = max(res[-1].end, tmp[i].end)
            else:
                res.append(tmp[i])
                
        return res