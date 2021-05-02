class Solution:
    """
    @param s: a string
    @param dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        if not s:
            return 0
        if not dict:
            return len(s)

        res, queue, seen = float('inf'), [s], set()

        while queue:
            cur = queue.pop(0)

            for substring in dict:
                new = cur
                found = cur.find(substring)

                while found != -1:
                    idx = cur.index(substring, found)
                    new = cur[:idx] + cur[idx+len(substring):]

                    if new not in seen: 
                        seen.add(new)
                        queue.append(new)

                        if res > len(new):
                            res = len(new)
                            
                    found = cur.find(substring, idx+1)                    
                    
                if not res:
                    return 0

        return res