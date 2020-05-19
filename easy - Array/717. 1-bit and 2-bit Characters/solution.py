class Solution:
    # my solution
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        while 0 in bits:
            if bits: == [0]
                return True
            elif bits[0:2] == [1, 0] or bits[0:2] == [1, 1]:
                bits = bits[2:]
            elif bits[0] == 0:
                bits = bits[1:]
                
        return False
    
    # better solution
    # https://leetcode.com/problems/1-bit-and-2-bit-characters/discuss/109011/python-solution-easy
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)-1
        
        while i < n:
            if bits[i] == 1:
                i += 2
            else:
                 i += 1
                    
        return i == n