class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph   = defaultdict(list)
        for i , j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(graph  ,  source ,destination ):
            stack = [source]
            visited = set()
            visited.add(source)
            while stack:
                node  =  stack.pop()
                if node ==  destination:
                    return True 
                for i in graph[node]:
                    if i not in visited:
                        visited.add(i)
                        stack.append(i)
            return False
        if dfs(graph  , source , destination):
            return True
        return False
            