class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        # write your code here
        len_A, len_B, res = len(A), len(B), ''
        
        if len_A < len_B:
            A = '0' * (len_B - len_A) + A
        else:
            B = '0' * (len_A - len_B) + B
            
        for a, b in zip(A, B):
            res += str(int(a) + int(b))
            
        return res