class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph   = defaultdict(list)
        indegree  = [0] * n
        for a , b in relations:
            a-=1
            b-=1
            graph[a].append(b)
            indegree[b] += 1
        

        queue =  deque()
        dp   = [ 0 ]  * n
        for i in  range(n):
            if indegree[i] ==  0:
                queue.append(i)
                dp[i]  = time[i]
        
        while queue:
            node  = queue.popleft()

            for child in graph[node]:
                dp[child]  =  max(dp[child]  , dp[node] + time[child] )
                indegree[child] -=  1
                if indegree[child]  == 0:
                    queue.append(child)

        return max(dp)



        