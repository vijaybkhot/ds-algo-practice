class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        
        elif self.rank[rootY] > self.rank[rootX]:
            self.parent[rootX] = rootY
        
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges)+1)
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
