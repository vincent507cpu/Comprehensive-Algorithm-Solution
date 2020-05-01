class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        lst = str.split()

        combo = zip(pattern, lst)
        
        return len(set(pattern)) == len(set(lst)) == len(set(combo)) and len(pattern) == len(lst)