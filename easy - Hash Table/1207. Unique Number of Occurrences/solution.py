class Solution:
    # my initial solution, 166 ms on 5 tests
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct = {}
        
        for n in arr:
            dct[n] = dct.get(n, 0) + 1
            
        return len(dct.values()) == len(set(dct.values()))
    
    # my second solution, thought improved but actually slower: 176 ms on 5 test
    # I realized the reason: I need to iterate the list len(arr) times here,
    # while I just need to iterate the list one time above
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct = {}
        
        for n in set(arr):
            count = arr.count(n)
            if count in dct.values():
                return False
            dct[n] = count
            
        return True