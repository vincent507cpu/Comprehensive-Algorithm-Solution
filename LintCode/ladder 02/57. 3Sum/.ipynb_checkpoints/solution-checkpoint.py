class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        res = []
        
        for i in range(len(numbers) - 2):
            if i and numbers[i] == numbers[i - 1]:
                continue
            
            if numbers[i] > 0:
                break
            
            l, r = i + 1, len(numbers) - 1
            
            while l < r:
                if numbers[i] + numbers[l] + numbers[r] < 0:
                    l += 1
                elif numbers[i] + numbers[l] + numbers[r] > 0:
                    r -= 1
                else:
                    res.append([numbers[i], numbers[l], numbers[r]])
                    while l < len(numbers) - 1 and numbers[l] == numbers[l + 1]:
                        l += 1
                    while numbers[r] == numbers[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                    
        return res