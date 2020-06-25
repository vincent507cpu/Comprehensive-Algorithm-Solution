# https://leetcode.com/problems/shift-2d-grid/discuss/434335/Python3%3A-2-simple-approaches-with-explanations-(by-creating-a-vector)

'''
Algorithm:

put the matrix row by row to a vector.
rotate the vector k times.
put the vector to the matrix back the same way.
The second step is the same as problem #189 (Rotate an Array), and can be solved in many ways, but here we consider two approaches that are simple and have reasonable time and space complexities:
(a) direct shift approach
(b) reverse approach

As an example of Approach (a), imagine we want to rotate the vector [1, 2, 3, 4, 5, 6, 7] for k = 3 times. We just need to add these two subsets of the vector, respectively: last k elements and first len(vec)-k elements:
[5, 6, 7] + [1, 2, 3, 4] = [5, 6, 7, 1, 2, 3, 4]

An example of Approach (b):
reverse all elements : [7, 6, 5, 4, 3, 2, 1]
reverse first k elements : [5, 6, 7, 4, 3, 2, 1]
reverse last len(vec)-k elements : [5, 6, 7, 1, 2, 3, 4]

Although approach (a) seems simpler, it take additional space (needs an extra vector in addition to the vector created in step 1). Approach (b) might need extra code lines, but does not take additional space.

Python3 codes:

Approach (a), direct shift:
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        #dimensions:
		NR = len(grid)
        NC = len(grid[0])
        vec = [0] * NR * NC #initialize the vector.
        #If k is greater than the length of vector, 
		#the shift will repeat itself in a cycle; 
		#hence, we only care about the remainder.
        k = k % (NR * NC)  
        
		#step 1: put the matrix row by row to the vector.
        for i in range(NR):
            for j in range(NC):
                vec[i * NC + j] = grid[i][j]
				
        #step 2: rotate vector k times by direct shift approach
        vec = vec[-k:] + vec[:-k]
		
        # step 3: put vector to matrix back the same way
        for i in range(NR):
            for j in range(NC):
                grid[i][j] = vec[i * NC + j]
        return grid
    
    '''
    Approach (b), reverse method: (Note that only step 2 has changed):
    '''
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # dimensions:
        NR = len(grid)
        NC = len(grid[0])
        vec = [0] * NR * NC #initialize the vector.
        # If k is greater than the length of vector, 
		# the shift will repeat itself in a cycle; 
		# hence, we only care about the remainder.
        k = k % (NR * NC)
		
        #step 1: put the matrix row by row to the vector.
        for i in range(NR):
            for j in range(NC):
                vec[i * NC + j] = grid[i][j]
				
        #step 2: rotate vector k times by reverse approach.
        self.Rev(vec, 0, NR * NC - 1) #reverse all elements.
        self.Rev(vec, 0, k-1)       #reverse first k elements.
        self.Rev(vec, k, NR * NC - 1) #revere last len(vec)-k elements. 
        
        #step 3: put the vector to the matrix back the same way.
        for i in range(NR):
            for j in range(NC):
                grid[i][j] = vec[i * NC + j]
        return grid
		
    # This function returns the reverse a subset of the vector,
	# bound by "left" and "right" elements
    def Rev(self, vec, left, right):
        while left < right:
            vec[left], vec[right] = vec[right], vec[left]
            left += 1 
            right -= 1