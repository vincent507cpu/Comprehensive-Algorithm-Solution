class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    # concisest solution
    # https://leetcode.com/problems/minimum-index-sum-of-two-lists/discuss/322322/2-lines-python
        
        dct = {x: list1.index(x) + list2.index(x) for x in set(list1) & set(list2)}
            
        return [key for key in dct.keys() if dct[key] == min(dct.values())]
    
    # fastest solution
    # https://leetcode.com/problems/minimum-index-sum-of-two-lists/discuss/534789/Python3-148ms-94.77-Hashmap
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dct1 = {res: i for i, res in enumerate(list1)}
        dct2 = {res: i + dct1[res] for i, res in enumerate(list2) if res in dct1}

        MIN = float('inf')
        res = []

        for key, val in dct2.items():
            if val < MIN:
                res = [key]
                MIN = val
            elif val == MIN:
                res.append(key)

        return res