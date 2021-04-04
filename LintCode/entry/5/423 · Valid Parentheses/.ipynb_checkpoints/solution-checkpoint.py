class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        if len(s) % 2:
            return False

        dct = {')':'(', '}':'{', ']':'['}
        stack = []

        for p in s:
            if p in dct.values():
                stack.append(p)
            else:
                if not stack or dct[p] != stack[-1]:
                    return False
                else:
                    stack.pop()

        return not bool(stack)