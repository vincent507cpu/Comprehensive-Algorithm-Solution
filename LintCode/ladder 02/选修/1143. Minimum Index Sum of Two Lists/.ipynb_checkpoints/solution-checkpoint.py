class Solution:
    """
    @param list1: a list of strings
    @param list2: a list of strings
    @return: the common interest with the least list index sum
    """
    def findRestaurant(self, list1, list2):
        # Write your code here
        dct = {}
        
        for i, name in enumerate(list1):
            dct[name] = [i]

        for j, name in enumerate(list2):
            if name not in dct:
                continue
            dct[name].append(j)
            
        dct = {key: sum(val) for key, val in dct.items() if len(val) == 2}
        
        return [key for key, val in dct.items() if val == min(dct.values())]