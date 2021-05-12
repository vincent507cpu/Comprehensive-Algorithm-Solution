class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, targer):
        # write your code here
        A = sorted(A)
        # used = [False] * len(A)
        res = []
        self.dfs(A, 0, [], res, k, targer)
        return res

    def dfs(self, A, index, nums, res, k, targer):
        if not k and not targer:
            res.append(nums[:])
            return
        if not k or not targer:
            return

        for i in range(index, len(A)):
            nums.append(A[i])
            self.dfs(A, i + 1, nums, res, k - 1, targer - A[i])
            nums.pop()