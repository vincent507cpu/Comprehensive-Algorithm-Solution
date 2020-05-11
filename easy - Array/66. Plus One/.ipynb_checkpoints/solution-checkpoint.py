class Solution:
    # my initial solution
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join([str(i) for i in digits])
        num = int(num) + 1
        num = str(num)
        return [int(s) for s in num]
    
    # a slightly better solution
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        
        for i in range(len(digits)-1, 0, -1):
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i-1] += 1
            
        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits
            
        return digits
    
    # recursion
    # https://leetcode.com/problems/plus-one/discuss/24090/Python-simple-solution-using-recursion
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]
        elif digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits = self.plusOne(digits[:-1])
            digits.append(0)
        return digits
    
    # better recursion from same page
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits or [0]
        num = digits.pop()
        
        if num == 9:
            return self.plusOne(digits) + [0]
        else:
            return digits + [num+1]
        
    # iteration
    # https://leetcode.com/problems/plus-one/discuss/24349/Simple-Python-O(n)-Solution-without-converting-to-a-number
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + 1 if digits[i] < 9 else 0
            if digits[i]:
                return digits
            
        digits.insert(0, 1)
        
        return digits