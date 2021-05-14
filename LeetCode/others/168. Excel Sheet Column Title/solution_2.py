class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        
        while columnNumber:
            res += chr((columnNumber - 1) % 26 + 65)
            columnNumber = (columnNumber - 1) // 26
            
        return res[::-1]