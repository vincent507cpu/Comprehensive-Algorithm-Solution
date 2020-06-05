class Solution:
    '''
    Since we can use infinite steps to change,
    we only need to make sure that the counts of each number equal,
    which makes a dictionary an ideal solution.
    '''
    
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return self.combination(target) == self.combination(arr)
    
    def combination(self, x):
        dct = {}
        
        for n in x:
            dct[n] = dct.get(n, 0) + 1
            
        return dct
    
    # use collections.Counter
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(target) == collections.Counter(arr)