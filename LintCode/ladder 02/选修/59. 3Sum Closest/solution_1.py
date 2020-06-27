# O(n^2) time, O(n) space

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        res = []
        
        for i in range(len(numbers) - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if numbers[left] + numbers[right] + numbers[i] > target:
                    res.append(numbers[left] + numbers[right] + numbers[i])
                    right -= 1
                else:
                    res.append(numbers[left] + numbers[right] + numbers[i])
                    left += 1
                    
        return sorted(res, key=lambda x:abs(x - target))[0]