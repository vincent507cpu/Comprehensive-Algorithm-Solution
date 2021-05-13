class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        res, carry = '', 0
        
        while i >= 0 or j >= 0:
            total = carry
            if i >= 0:
                total += int(a[i])
            if j >= 0:
                total += int(b[j])
            res += str(total % 2)
            carry = total // 2
            
            i -= 1
            j -= 1
            
        if carry:
            res += '1'
        return res[::-1]