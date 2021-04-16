class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if not A:
            return 0
            
        left = self.find_bandry(A, target, 0, len(A) - 1)
        right = self.find_bandry(A, target, 0, len(A) - 1, False)

        return 0 if left == -1 else right - left + 1

    def find_bandry(self, A, target, start, end, left=True):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                if left:
                    end = mid
                else:
                    start = mid

        if left:
            if A[start] == target:
                return start
            if A[end] == target:
                return end
        else:
            if A[end] == target:
                return end
            if A[start] == target:
                return start
            
        return -1