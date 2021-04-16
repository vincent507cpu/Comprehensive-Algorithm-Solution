class TwoSum:
    def __init__(self):
        self.lst = []
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.lst.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        self.lst.sort()
        left, right = 0, len(self.lst) - 1

        while left < right:
            while left < right and self.lst[left] + self.lst[right] < value:
                left += 1
            while left < right and self.lst[left] + self.lst[right] > value:
                right -= 1
            if left < right and self.lst[left] + self.lst[right] == value:
                return True

        return False