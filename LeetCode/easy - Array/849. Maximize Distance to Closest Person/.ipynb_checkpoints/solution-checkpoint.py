# https://leetcode.com/problems/maximize-distance-to-closest-person/discuss/165302/Python-O(n)-Solution
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # left记载当前位置左边第一个1的位置
        # count进行0的计数
        # _max_distance维护最大距离返回值
        left, count, long = -1, 0, 1
        
        for i, n in enumerate(seats):
            if not n: 
                count += 1
            else:
                if left < 0:
                    # 左边没有1最大距离就是count
                    dist = count
                else:
                    # 左边有1最大距离就是一半左右
                    # 奇数个0正好在中间
                    # 偶数个0要比一半小1
                    dist = count // 2 + count % 2
                # 重置左边第一个1的位置
                # 遇到1重新计数0的个数
                left, count = i, 0
                # 更新最大距离
                long = max(long, dist)
        # 末尾一连串0的情况也可能刷新最大距离
        return max(long, count)