class Solution:
    """
    @param string: A string
    @return: whether the string is a valid parentheses
    """
    def matchParentheses(self, string):
        # write your code here
        if len(string) % 2:
            return False

        stack = []

        for p in string:
            if p == '(':
                stack.append(p)
            elif p == ')':
                if not stack:
                    return False
                else:
                    stack.pop()
            else:
                return False

        return not bool(stack)