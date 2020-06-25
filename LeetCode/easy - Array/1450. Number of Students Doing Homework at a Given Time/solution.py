class Solution:
    # use zip, takes 52 ms
    class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        
        for start, end in zip(startTime, endTime):
            if queryTime in list(range(start, end + 1)):
                res += 1
                
        return res
    
    # diectly compare, takes 36 ms
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                res += 1
                
        return res
    
    # list comprehension, takes 32 ms
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(a <= queryTime <= b for a, b in zip(startTime, endTime))