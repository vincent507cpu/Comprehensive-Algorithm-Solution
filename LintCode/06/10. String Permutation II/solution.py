class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        chars = sorted(list(str))
        visited = [False] * len(chars)
        result = []
        self.dfs(chars, visited, [], result)
        return result
        
    def dfs(self, chars, visited, permutation, result):
        if len(permutation) == len(chars):
            result.append(''.join(permutation))
            return
        
        for i in range(len(chars)):
            if visited[i]:
                continue
            if i and chars[i] == chars[i - 1] and not visited[i - 1]:
                continue
            
            visited[i] = True
            permutation.append(chars[i])
            self.dfs(chars, visited, permutation, result)
            permutation.pop()
            visited[i] = False