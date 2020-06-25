# comprehensive solution

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # https://leetcode.com/problems/jewels-and-stones/discuss/527360/Several-Python-solution.-w-Explanation
        jewel = set(J)
        return sum( 1 for item in S if item in jewel )
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        # https://leetcode.com/problems/jewels-and-stones/discuss/527360/Several-Python-solution.-w-Explanation
        return sum( S.count(jewel) for jewel in J )
        
    def numJewelsInStones(self, J: str, S: str) -> int:
        # https://leetcode.com/problems/jewels-and-stones/discuss/?currentPage=1&orderBy=most_votes&query=
        return sum(s in J for s in S)
        
    def numJewelsInStones(self, J: str, S: str) -> int:
        # https://leetcode.com/problems/jewels-and-stones/discuss/?currentPage=1&orderBy=most_votes&query=
        return sum(map(J.count, S))