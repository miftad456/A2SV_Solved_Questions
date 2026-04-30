class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph   = defaultdict(list)
        indegree  = [0]  * n
        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1
        queue  = deque()

        for i in range(n):
            if indegree[i]  == 0 :
                queue.append(i)
        
        ansector  = [set() for i in range(n)]

        while queue:
            node  =  queue.popleft()
            for child in  graph[node]:
                ansector[child].add(node)

                ansector[child].update(ansector[node])

                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        return [sorted(list(a)) for a in ansector]
        

        
        