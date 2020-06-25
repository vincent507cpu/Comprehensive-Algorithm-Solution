class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        if not str:
            return None
            
        once = []
        app = []
        
        for l in str:
            if l not in once and l not in app:
                once.append(l)
                app.append(l)
            elif l in once and l in app:
                once.remove(l)
                
        return once[0]