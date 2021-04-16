class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        if len(s) < 4 or len(s) > 12:
            return []
            
        res = []
        self.dfs(s, 0, '', res)
        return res
        
    def dfs(self, s, pieces, add, res):
        if pieces == 4 and not s:
            res.append(add[1:])
            return
        
        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], pieces + 1, add + '.' + s[:i], res)
          
                if s[0] == '0':
                    break