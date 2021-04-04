class Solution:
    """
    @param n: an integer
    @return: return all prime numbers within n.
    """
    def prime(self, n):
        # write your code here
        if n < 2:
            return []
            
        res = [2]

        for i in range(3, n+1):
            flag = False
            for j in range(2, int(i**0.5)+1):
                if not i % j:
                    flag = True
                    break
            if not flag:
                res.append(i)

        return res