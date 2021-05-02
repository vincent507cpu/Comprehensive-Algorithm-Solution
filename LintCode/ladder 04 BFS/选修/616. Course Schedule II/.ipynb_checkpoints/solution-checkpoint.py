class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        prereq = {i:[] for i in range(numCourses)}
        degree = [0 for _ in range(numCourses)]

        for cur, pre in prerequisites:
            prereq[pre].append(cur)
            degree[cur] += 1

        queue = []
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)

        order = []

        while queue:
            node = queue.pop(0)
            order.append(node)
            for val in prereq[node]:
                degree[val] -= 1
                if degree[val] == 0:
                    queue.append(val)

        return order if len(order) == numCourses else []