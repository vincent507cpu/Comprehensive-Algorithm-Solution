class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        carry, res = 0, ''
        for i in reversed(range(max_len)):
            carry += (1 if a[i] == '1' else 0)
            carry += (1 if b[i] == '1' else 0)
            res += '1' if (carry % 2) else '0'
            carry //= 2
        
        return '1' + res[::-1] if carry else res[::-1]