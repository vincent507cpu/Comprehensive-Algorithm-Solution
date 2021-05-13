class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        i = 1
        
        while i < len(intervals):
            ll = intervals[i - 1][0]
            lr = intervals[i - 1][1]
            rl = intervals[i][0]
            rr = intervals[i][1]
            
            if ll <= rl <= lr:
                intervals[i - 1][1] = max(lr, rr)
                del intervals[i]
            else:
                 i += 1
                    
        return intervals