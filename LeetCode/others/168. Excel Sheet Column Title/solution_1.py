class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        
        dct = {i: l for i, l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)}
        
        while columnNumber > 26:
            count = columnNumber % 26
            if not count:
                res += 'Z'
                columnNumber = columnNumber // 26 - 1
            else:
                res += dct[count]
                columnNumber //= 26
                
        res += dct[columnNumber]
        return res[::-1]