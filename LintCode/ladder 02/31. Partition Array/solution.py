class Solution:
    class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        self.sort(colors, 0, len(colors) - 1, 1, k)
        
    def sort(self, colors, left, right, colorFrom, colorTo):
        if colorFrom >= colorTo:
            return
        
        if left >= right:
            return
        
        colorMid = (colorFrom + colorTo) // 2
        l,r, pos = left, right, left
        
        for i in range(l, r + 1):
            if colors[i] <= colorMid:
                colors[pos], colors[i] = colors[i], colors[pos]
                pos += 1
                
        self.sort(colors, left, pos - 1, colorFrom, colorMid)
        self.sort(colors, pos, right, colorMid + 1, colorTo)