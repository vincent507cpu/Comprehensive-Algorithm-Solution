class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        if not s or not dict:
            return 0
            
        lower_dict = set()
        for piece in dict:
            lower_dict.add(piece.lower())
        max_len = max([len(piece) for piece in dict])
        return self.memo_search(s.lower(), lower_dict, 0, max_len, {})
        
    def memo_search(self, s, dict, index, max_len, memo):
        if index == len(s):
            return 1
            
        if index in memo:
            return memo[index]
            
        memo[index] = 0
        
        for i in range(index, len(s)):
            if i + 1 - index > max_len:
                break
            word = s[index:i + 1]
            if word not in dict:
                continue
            memo[index] += self.memo_search(s, dict, i + 1, max_len, memo)
            
        return memo[index]