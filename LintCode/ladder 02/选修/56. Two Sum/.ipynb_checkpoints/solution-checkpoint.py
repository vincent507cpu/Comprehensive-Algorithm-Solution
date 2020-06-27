class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        dct = {}
        for i, num in enumerate(numbers):
            if target - num not in dct:
                dct[num] = i
            else:
                return [dct[target - num], i]