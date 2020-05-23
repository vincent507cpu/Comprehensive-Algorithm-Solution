class Solution:
    # my solution
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dct = {}
        res, others = [], []
        
        for n in arr1:
            if n in set(arr2):
                dct[n] = dct.get(n, 0) + 1
            else:
                others.append(n)
                
        for n in arr2:
            res += [n] * dct[n]
            
        return res + sorted(others)
    
    # more concise solution
    # https://leetcode.com/problems/relative-sort-array/discuss/334585/Python-Straight-Forward-1-line-and-2-lines
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # You create hashmap of indexes of elements in arr2, because you are going to ask for it everytime when sorting. So in case you have something like [2,2,2,2,2,2,2,1] you won't go and perform same index search everytime.
        k = {b: i for i, b in enumerate(arr2)}
        
        # you are sorting initial list arr1 with key function that will get index of element in arr1 from hashmap that you already created and in case it's not there it will add 1000 to the element itself so it will put elements that are in arr1 but not in arr2 after all the elements in resulting list. You can do it as you know that 0 <= arr1[i], arr2[i] <= 1000
        return sorted(arr1, key=lambda a: k.get(a, 1000 + a))