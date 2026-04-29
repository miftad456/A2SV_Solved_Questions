from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        queue   = deque()
        for i in range(len(indegree)):
            if indegree[i]  == 0:
                queue.append(i)
        order  = []
        while queue:
            node   =  queue.popleft()
            order.append(node)
            for  child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        print(order)
        
        return order if len(order) ==  numCourses else []


        
        