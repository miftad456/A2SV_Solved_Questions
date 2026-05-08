class UnionFind:
    def __init__(self ,n):
        self.parents = [i for i in range(n)]
        self.rank =  [0] * n
    def find(self , x):
        while x != self.parents[x]:
            x =  self.parents[x]
        return x
    def union(self, x ,y):
        root_x = self.find(x)
        root_y  = self.find(y)
        if root_x != root_y:
            if self.rank[root_x]  > self.rank[root_y]:
                self.parents[root_y]  = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.parents[root_x]  = root_y
            else:
                self.parents[root_y]  = root_x
                self.rank[root_x] += 1
                
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = UnionFind(n)
        numberOfComponents = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] and dsu.find(i) != dsu.find(j):
                    numberOfComponents -= 1
                    dsu.union(i, j)
        return numberOfComponents
            
    
        