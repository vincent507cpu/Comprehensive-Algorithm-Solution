class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]

        left = self.find_bandry(A, target, 0, len(A) - 1)
        if left == -1:
            return [-1, -1]
        right = self.find_bandry(A, target, left, len(A) - 1, False)
        return [left, right]

    def find_bandry(self, A, target, start, end, left=True):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
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