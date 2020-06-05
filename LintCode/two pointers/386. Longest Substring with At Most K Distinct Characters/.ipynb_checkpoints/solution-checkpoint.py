class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    # two pointers
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0 or len(s) == 0:
            return 0

        dct = {}
        left, right = 0, 0
        unique, ans = 0, 0
        
        while right < len(s):
            # 统计right指向的字符
            # 当字符在窗口内第一次出现时，字符种类数+1，该字符出现次数+1
            if s[right] not in dct or dct[s[right]] == 0:
                unique += 1
                dct.setdefault(s[right], 0)
            dct[s[right]] += 1
            right += 1
            
            # 向右移动left，保持窗口内只有k种不同的字符
            while unique > k:
                dct[s[left]] -= 1;
                if dct[s[left]] == 0:
                    unique -= 1
                left += 1
            # 更新答案
            ans = max(ans, right - left)
        
        return ans