# https://leetcode.com/problems/friends-of-appropriate-ages/discuss/565958/python-counting-and-then-one-pass

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        lst = [0] * 121
        res = 0
        
        for n in ages:
            lst[n] += 1

        for i, n in enumerate(lst):
            if n:
                start = int(i * 0.5 + 7)
                res += sum(lst[start+1:i] * n)
                    
                if start < i:
                    res += n * (n - 1)
                    
        return res
    
    # more straightforward but slower
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1

        res = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
#                 if ageA < 100 < ageB: continue
                res += countA * countB
                if ageA == ageB: res -= countA

        return ans