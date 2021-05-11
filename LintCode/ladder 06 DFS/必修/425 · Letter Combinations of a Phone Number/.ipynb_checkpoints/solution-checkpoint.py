class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []

        self.mapping = {'2':'abc',
                        '3':'def',
                        '4':'ghi',
                        '5':'jkl',
                        '6':'mno',
                        '7':'pqrs',
                        '8':'tuv',
                        '9':'wxyz'}
        res = []
        self.dfs(digits, 0, [], res)
        return res

    def dfs(self, digits, idx, chars, res):
        if idx == len(digits):
            res.append(''.join(chars))
            return

        for letter in self.mapping[digits[idx]]:
            chars.append(letter)
            self.dfs(digits, idx+1, chars, res)
            chars.pop()