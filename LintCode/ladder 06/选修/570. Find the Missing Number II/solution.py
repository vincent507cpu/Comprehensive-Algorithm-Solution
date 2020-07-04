class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        # write your code here
        seen = [False] * (n + 1)
        ans = self.dfs(str, n, 0, seen)
        return ans
        
    def dfs(self, str, n, index, seen):
        if index == len(str):
            for i in range(1, len(seen)):
                if not seen[i]:
                    return i
            
        for i in [1, 2]:
            if index + i > len(str):
                continue
            
            tmp = int(str[index:index + i])
            if not (i == 2 and tmp < 10) and self.is_valid(tmp, seen, n):
                seen[tmp] = True
                x = self.dfs(str, n, index + i, seen)
                if x:
                    return x
                seen[tmp] = False
                
    def is_valid(self, tmp, seen, n):
        if tmp == 0 or tmp > n:
            return False
            
        if seen[tmp]:
            return False
            
        return True