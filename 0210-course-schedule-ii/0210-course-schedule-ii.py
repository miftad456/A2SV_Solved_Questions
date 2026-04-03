class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
        graph =  defaultdict(list)

        visiting =  set()
         
        visited  =  set()

        order  = []
        def dfs(node):
            nonlocal order
            if node in visiting:
                return False
            if node in visited :
                return True
            visiting.add(node)
            for nr in graph[node]:
                if not dfs(nr):
                    return False
            visiting.remove(node)
            visited.add(node)
            order.append(node)
            return True

        for a, b  in prerequisites:
            graph[b] .append(a)
       

        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return []
        return order[::-1]



        