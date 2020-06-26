class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        prereq = {i: [] for i in range(numCourses)}
        inDegree = [0 for _ in range(numCourses)]
        
        for course, pre in prerequisites:
            prereq[pre].append(course)
            inDegree[course] += 1
            
        queue, res = [], []
        for i in range(numCourses):
            if not inDegree[i]:
                queue.append(i)
                
        while queue:
            node = queue.pop(0)
            res.append(node)
            
            for x in prereq[node]:
                inDegree[x] -= 1
                if inDegree[x] == 0:
                    queue.append(x)
                    
        return res if len(res) == numCourses else []