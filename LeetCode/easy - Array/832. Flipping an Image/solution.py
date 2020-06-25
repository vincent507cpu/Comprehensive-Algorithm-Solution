class Solution:
    # my solution
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for i in range(len(row) // 2):
                row[i], row[-i-1] = row[-i-1], row[i]
                
            for i in range(len(row)):
                row[i] = 0 if row[i] == 1 else 1
                
        return A
    
    # list comprehension
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[0 if x == 1 else 1 for x in num[::-1]] for num in A]