# My solution
# https://leetcode.com/problems/number-of-boomerangs/discuss/611743/python3-solution-with-explanations

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3: # tuple must have at least 3 elements
            return 0
        
        res = 0
        # idea: iterate all points, calculate distances between each point and other points,
		# put distances in dictionaries. If there are values greater than 1, 
		# meaning there are multiple points have the same distance with it.
		# Since order matters, total combination numbers would be val * (val - 1).
        for p1 in points:
            tmp = {}
            for p2 in points:
                d = self.dist(p1, p2)
                tmp[d] = tmp.get(d, 0) + 1
            for val in [val for val in tmp.values() if val > 1]:
                res += val * (val - 1)
                
        return res
        
    def dist(self, p1, p2): # calculate pointwise distance
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2