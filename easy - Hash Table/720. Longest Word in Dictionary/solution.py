# solution
# https://leetcode.com/problems/longest-word-in-dictionary/discuss/367203/easy-peasy-python-solution-using-sorting-and-set

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        st, res = set(), ""
        st.add("") # set('') will be equal to set()
        for word in words:
            if word[:-1] in st:
                if len(word) > len(res):
                    res = word
                st.add(word)

        return res