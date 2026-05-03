class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph   =  defaultdict(list)
        if n == 1:
            return [0]
        indegree  = [0]  * n 
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] +=  1
            indegree[v]  += 1
        

        leaves = deque()
        for i in  range(n):
            if indegree[i] ==  1:
                leaves.append(i)
        

        remain  = n

        while remain > 2:
            size  = len(leaves)
            remain -= size

            for i in range(size):
                leaf  = leaves.popleft()

                for i in graph[leaf]:
                    indegree[i] -=  1
                    if indegree[i] == 1:
                        leaves.append(i)
        return list(leaves)
        

