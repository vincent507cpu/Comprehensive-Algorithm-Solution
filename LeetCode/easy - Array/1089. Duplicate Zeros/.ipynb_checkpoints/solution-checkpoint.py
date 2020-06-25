class Solution:
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