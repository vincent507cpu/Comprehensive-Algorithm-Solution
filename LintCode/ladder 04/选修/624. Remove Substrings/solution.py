class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        length = float('inf')
        seen = set()
        
        queue = [s]
        
        while queue:
            string = queue.pop(0)
            
            for substitute in dict:
                n_chars = len(substitute)
                
                if string == substitute:
                    return 0
                
                found = string.find(substitute)
                while found != -1:
                    new = string[:found] + string[found + n_chars:]
                    if new not in seen:
                        queue.append(new)
                        seen.add(new)
                        if length > len(new):
                            length = len(new)
                    found = string.find(substitute, found + 1)

        return length