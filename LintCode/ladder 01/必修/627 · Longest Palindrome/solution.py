# create a set, iterate string.
# a letter in set means if appears twice so far,
# add 2 to res and remove it from set, otherwise add it into set.
# after iteration, if set is empty, return res. otherwise return res + 1

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        res = 0
        left = set()

        for l in s:
            if l in left:
                res += 2
                left.remove(l)
            else:
                left.add(l)

        return res + 1 if left else res