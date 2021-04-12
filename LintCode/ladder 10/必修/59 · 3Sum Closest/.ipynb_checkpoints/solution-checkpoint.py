class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        res = float('inf')
        
        for i in range(len(numbers) - 2):
            l, r = i + 1, len(numbers) - 1

            while l < r:
                total = numbers[i] + numbers[l] + numbers[r]

                if total < target:
                    if abs(target - total) < abs(target - res):
                        res = total
                    l += 1
                elif total > target:
                    if abs(target - total) < abs(target - res):
                        res = total
                    r -= 1
                else:
                    return total

        return res