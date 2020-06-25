class Solution:
    # my solution
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dct = {}
        res = 0
        
        for i, n in enumerate(time):
            dct[n % 60] = dct.get(n%60, []) + [i]
            
        print(dct)
        for left in dct.keys():
            if left % 60 == 0 or left % 60 == 30:
                res += len(dct[left]) * (len(dct[left])-1) / 2
            elif 60 - left in dct.keys():
                res += len(dct[left]) * len(dct[60-left]) / 2
                
        return int(res)
    
    # optimal solution
    # https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/642553/Python-O(n)-with-simple-math-explanation
    '''
    1. We are given that (a+b) % c = (a%c + b%c) % c = 0
    2. So, (a%c + b%c) = n*c where n is an integer multiple.
    3. We know that (a%c + b%c) has max of c-1 + c-1 = 2c - 2 < 2c
    4. But rhs says it has to be an integer multiple of c, and we are bounded by the fact that this has to be less than 2. so only option is either 0 or 1 (no negative cuz song durations arent negative)
    5. So given a, we look for b%c = n*c - a%c, where n = 0 or 1.
    6. Can do this easily with hashmap, for each number a, take modulo of it, look for that in the hashmap where it maps number of occurance of b%c.
    7. Update answer and the hashmap accordingly.
    '''
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        dct = {}
        
        for t in time:
            t_mod = t % 60
            
            find = 0 if t_mod == 0 else 60 - t_mod
            res += dct.get(find, 0)
            dct[t_mod] = dct.get(t_mod, 0) + 1
            
        return res