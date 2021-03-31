class Solution:
    """
    @param c: A character.
    @return: The character is alphanumeric or not.
    """
    def isAlphanumeric(self, c):
        # write your code here
        return c.isalpha() or c.isdigit()