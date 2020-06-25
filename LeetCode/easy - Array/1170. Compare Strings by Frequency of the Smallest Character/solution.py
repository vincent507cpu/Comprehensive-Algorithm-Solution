class Solution:
    # my solution
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queries_c = self.count(queries)
        words_c = sorted(self.count(words))
        res = []
        for query_c in queries_c:
            res.append(sum([1 for x in words_c if query_c < x]))
        return res
    
    def count(self, queries):
        lst = []
        for query in queries:
            lst.append([query.count(x) for x in query if x == min([x for x in query])])
        return lst
    
    # faster solution
    # https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/discuss/401039/Python-Simple-Code-Memory-efficient
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            n = sorted(list(s))[0]
            return s.count(n)
        
        queries = [f(s) for s in queries]
        words = [f(s) for s in words]
        
        
        res = []
        for query in queries:
            tmp = 0
            for word in words:
                if query < word:
                    tmp += 1
            res.append(tmp)
            
        return res