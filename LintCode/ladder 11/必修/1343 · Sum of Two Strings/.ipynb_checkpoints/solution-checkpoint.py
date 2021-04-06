class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        # write your code here
        A, B = list(A), list(B)

        if len(A) < len(B):
            A = ['0'] * (len(B) - len(A)) + A
        else:
            B = ['0'] * (len(A) - len(B)) + B

        return ''.join([str(int(a) + int(b)) for a, b in zip(A, B)])