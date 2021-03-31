class Calculator:
    """
    @param a: An integer
    @param operator: A character, +, -, *, /.
    @param b: An integer
    @return: The result
    """
    def calculate(self, a, operator, b):
        # write your code here
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a // b