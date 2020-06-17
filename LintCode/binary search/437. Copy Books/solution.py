class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
            
        start, end = max(pages), sum(pages)
        
        while start + 1 < end:
            mid = (start + end) // 2
            if self.getCopiers(pages, mid) <= k:
                end = mid
            else:
                start = mid
                
        if self.getCopiers(pages, start) <= k:
            return start
            
        return end

    def getCopiers(self, pages, limit):
        copiers = 1
        time = 0
        
        for page in pages:
            if time + page > limit:
                copiers += 1
                time = 0
            time += page
                
        return copiers