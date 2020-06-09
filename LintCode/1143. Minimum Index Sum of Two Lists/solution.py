class Solution:
    """
    @param list1: a list of strings
    @param list2: a list of strings
    @return: the common interest with the least list index sum
    """
    def findRestaurant(self, list1, list2):
        # Write your code here
        both = set(list1).intersection(set(list2))
        
        if len(both) == 1:
            return list(both)
        else:
            dct = {}
            for place in both:
                dct[place] = list1.index(place) + list2.index(place)
            return [key for key, val in dct.items() if val == min(dct.values())]