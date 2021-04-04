class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    def longestWords(self, dictionary):
        # write your code here
        res, length = [], 0

        for w in dictionary:
            if len(w) > length:
                length = len(w)
                res = [w]
            elif len(w) == length:
                res.append(w)

        return res