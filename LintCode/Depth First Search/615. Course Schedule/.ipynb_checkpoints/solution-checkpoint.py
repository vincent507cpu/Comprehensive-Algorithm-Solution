class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        prereq = {i: [] for i in range(numCourses)}
        inDegree = [0 for i in range(numCourses)]

        for course, pre in prerequisites:
            prereq[pre].append(course)
            inDegree[course] += 1
            
        queue, count = [], 0
            
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
                
        while queue:
            node = queue.pop(0)
            count += 1
            
            for course in prereq[node]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)
                    
        return count == numCourses