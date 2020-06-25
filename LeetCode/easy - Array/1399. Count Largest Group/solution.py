class Solution:
    # my solution
    def countLargestGroup(self, n: int) -> int:
        count = collections.Counter(self.sum_digits(s) for s in range(1, n+1))
        return sum(1 for val in count.values() if val== max(count.values()))
    
    def sum_digits(self, x):
        x = [s for s in str(x)]
        return sum(int(s) for s in x)
    
    '''Most frequent value is called →mode, and →statistics.multimode gives us all of them.'''
    # https://leetcode.com/problems/count-largest-group/discuss/563356/1-line-Python
    def countLargestGroup(self, n: int) -> int:
        return len(statistics.multimode(sum(map(int, str(i))) for i in range(1, n+1)))