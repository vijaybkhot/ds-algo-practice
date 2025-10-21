class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if x != self.parent[x]:
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
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        candidate1, candidate2 = None, None
        parents = {}

        # [   0, 0, 1, 1, 1, 0               ]

        for idx, edge in enumerate(edges):
            u, v = edge
            if v in parents:
                candidate1 = [parents[v], v]
                candidate2 = [u, v]
                break
            parents[v] = u
        
        uf = UnionFind()
        for u, v in edges:
            if candidate2 and candidate2 == [u, v]:
                continue
            
            if not uf.union(u, v):
                if candidate1:
                    return candidate1
                return [u, v]
        
        return candidate2


