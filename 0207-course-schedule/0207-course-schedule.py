class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i]  == 0:
                queue.append(i)
        order = 0
        while queue :
            node  = queue.popleft()
            order += 1
            for  child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        if order == numCourses:
            return True
        return False


