# 

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = [0] * 121
        res = 0
        
        for n in ages:
            cnt[n] += 1
            
        for i in range(121):
            if cnt[i]:
                low = int(i * 0.5 + 7)
                res += sum(cnt[i] * cnt[low+1:i])
                
                if low < i:
                    res += cnt[i] * (cnt[i] - 1)
                    
        return res