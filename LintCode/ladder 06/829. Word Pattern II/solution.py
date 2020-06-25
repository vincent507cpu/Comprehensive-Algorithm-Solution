class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        return self.is_match(pattern, str, {}, set())
        
    def is_match(self, pattern, str, mapping, used):
        if not pattern:
            return not str
            
        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if not str.startswith(word):
                return False
            return self.is_match(pattern[1:], str[len(word):], mapping, used)
            
        for i in range(len(str)):
            word = str[:i + 1]
            if word in used:
                continue
            
            used.add(word)
            mapping[char] = word
            
            if self.is_match(pattern[1:], str[i + 1:], mapping, used):
                return True
                
            del mapping[char]
            used.remove(word)
            
        return False