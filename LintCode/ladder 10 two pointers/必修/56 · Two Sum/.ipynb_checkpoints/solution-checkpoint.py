class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if not numbers:
            return -1

        dct = {}

        for i in range(len(numbers)):
            if target - numbers[i] not in dct:
                dct[numbers[i]] = i
            else:
                return [dct[target - numbers[i]], i]