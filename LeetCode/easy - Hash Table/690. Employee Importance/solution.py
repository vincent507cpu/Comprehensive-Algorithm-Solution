"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    # my solution (my 1st recruseion!)
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0

        for k in employees:
            if k.id == id:
                res += k.importance
                if not k.subordinates:
                    return res
                else:
                    for j in k.subordinates:
                        res += self.getImportance(employees, j)
                        
        return res
    
    # best solution
    # https://leetcode.com/problems/employee-importance/discuss/112611/3-liner-Python-Solution-(beats-99)
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        emps = {employee.id: employee for employee in employees}
        def dfs(id):
            subordinates_importance = sum([dfs(sub_id) for sub_id in emps[id].subordinates])
            return subordinates_importance + emps[id].importance
        return dfs(id)