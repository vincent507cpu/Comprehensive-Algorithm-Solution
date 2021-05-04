class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        in_degree = [0 for _ in range(numCourses)]
        prereq = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            in_degree[course] += 1
            prereq[pre].append(course)

        queue = [idx for idx, course in enumerate(in_degree) if not course]
        res = []

        while queue:
            node = queue.pop(0)
            res.append(node)

            for course in prereq[node]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        return res if len(res) == numCourses else []