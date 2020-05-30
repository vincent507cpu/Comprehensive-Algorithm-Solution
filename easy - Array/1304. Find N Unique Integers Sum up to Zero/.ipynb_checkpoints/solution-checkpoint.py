class Solution:
    # my solution
    def sumZero(self, n: int) -> List[int]:
        return list(range(n-1)) + [-sum(range(n-1))]