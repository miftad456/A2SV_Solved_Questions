class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path  = []
        result  = []
        def dfs(node):
            path.append(node)
            if node == len(graph)-1:
                result.append(path.copy())
            else:
                for nib in graph[node]:
                    dfs(nib)
            path.pop()
        dfs(0)
        return result

        