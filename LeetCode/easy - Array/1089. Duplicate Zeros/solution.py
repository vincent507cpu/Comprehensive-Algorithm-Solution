class Solution:
    # forward iteration
    # for loop
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        flag = True
        for i in range(len(arr)):
            if flag and arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop()
                flag = False
            else:
                flag = True
                
    # while loop
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop()
                i += 1
            i += 1
            
    # backward iteration
    # https://leetcode.com/problems/duplicate-zeros/discuss/322576/Python-3-real-in-place-solution
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0