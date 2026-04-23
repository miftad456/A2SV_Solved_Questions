class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1 for i in range(len(graph))]
       
        def dfs(graph , node):
            temp  = True
            for nbr in graph[node]:
                if colors[nbr] ==  -1:
                    if colors[node] == 0:
                        colors[nbr] = 1
                    else:
                        colors[nbr]  =  0
                    temp  = temp and dfs(graph , nbr)
                elif colors[node] ==  colors[nbr]:
                    return False
            return temp
        result = True
        for node in range(len(graph)):
            if colors[node] == -1:
                colors[node] = 0
                result = result and dfs(graph, node)

        return result