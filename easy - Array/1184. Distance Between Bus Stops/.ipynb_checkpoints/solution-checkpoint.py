class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            clockwise = sum(distance[start:destination])
            counter = sum(distance[:start]) + sum(distance[destination:])
        else:
            clockwise = sum(distance[destination:start])
            counter = sum(distance[:destination]) + sum(distance[start:])
        return min(clockwise, counter)
    
    # https://leetcode.com/problems/distance-between-bus-stops/discuss/377532/python-3-easy-to-understand
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
		a = min(start, destination)
		b = max(start, destination)
		return min(sum(distance[a:b]), sum(distance) - sum(distance[a:b]))