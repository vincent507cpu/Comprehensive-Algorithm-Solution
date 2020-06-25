

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # consulted https://leetcode.com/problems/powerful-integers/discuss/433344/Python-beats-99.6-and-100-in-two-ways-easy
        res, i, j = set(), 0, 0
        
        while x ** i < bound:
            tmp = x ** i
            
            while tmp + y ** j <= bound:
                res.add(tmp + y ** j)
                if y == 1: break
                j += 1
                
            if x == 1: break
            i += 1
            j = 0
            
        return list(res)
    
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # DFS: https://leetcode.com/problems/powerful-integers/discuss/216318/Python-DFS-solution
        res = set()
        stack = [(0, 0)]
        
        while stack:
            i, j = stack.pop(0)
            if x ** i + y ** j <= bound:
                res.add(x**i+y**j)
                if x != 1:
                    stack.append((i+1, j))
                if y != 1:
                    stack.append((i, j+1))
                    
        return list(res)