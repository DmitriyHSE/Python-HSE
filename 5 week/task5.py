'''
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/bus-routes/
'''

from collections import *


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        stopToRoute = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stopToRoute[stop].append(i)
        visited = set()
        queue = deque()
        queue.append(source)
        visited.add(source)
        buses = 0
        while queue:
            for i in range(len(queue)):
                stop = queue.popleft()
                if stop == target:
                    return buses
                for i in stopToRoute[stop]:
                    for next in routes[i]:
                        if next not in visited:
                            queue.append(next)
                            visited.add(next)
                    routes[i] = []
            buses += 1

        return -1
