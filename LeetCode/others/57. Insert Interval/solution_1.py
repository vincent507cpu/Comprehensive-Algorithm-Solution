class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        overlap = False
        # new = []
        
        while i < len(intervals) and not overlap:
            if newInterval[0] < intervals[i][0]:
                new = [newInterval[0]]
                overlap = True
            elif intervals[i][0] <= newInterval[0] <= intervals[i][1]:
                new = [intervals[i][0]]
                overlap = True
            else:
                res.append(intervals[i])
                i += 1
                
        while i < len(intervals) and overlap:
            if newInterval[1] < intervals[i][0]:
                new += [newInterval[1]]
                return res + [new] + intervals[i:]
            elif intervals[i][0] <= newInterval[1] <= intervals[i][1]:
                new += [intervals[i][1]]
                return res + [new] + intervals[i+1:]
            else:
                i += 1
                
        if not overlap:
            intervals.append(newInterval)
            return intervals
        else:
            new.append(newInterval[1])
            return res + [new]