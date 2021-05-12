class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        chars = sorted(str)
        visited = [False] * len(chars)
        res = []
        self.dfs(chars, [], visited, res)
        return res

    def dfs(self, chars, perm, visited, res):
        if len(perm) == len(chars):
            res.append(''.join(perm))
            return
        
        for i in range(len(chars)):
            if visited[i]:
                continue
            if i and chars[i] == chars[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            perm.append(chars[i])
            self.dfs(chars, perm, visited, res)
            visited[i] = False
            perm.pop()