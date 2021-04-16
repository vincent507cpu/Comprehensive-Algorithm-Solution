KEYBOARD = {
    '2': "abc",
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
            
        result = []
        self.dfs(digits, 0, [], result)
        return result
        
    def dfs(self, digits, index, chars, result):
        if len(chars) == len(digits):
            result.append(''.join(chars))
            return
        
        for letter in KEYBOARD[digits[index]]:
            chars.append(letter)
            self.dfs(digits, index + 1, chars, result)
            chars.pop()