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

        # Find node with two parents
        for idx, edge in enumerate(edges):
            u, v = edge
            if v in parents:
                candidate1 = [parents[v], v]
                candidate2 = [u, v]
                break
            parents[v] = u
        
        # Initiate Disjoint Set
        uf = UnionFind()

        for u, v in edges:
            if candidate2 and candidate2 == [u, v]:
                continue
            # If Cycle found
            if not uf.union(u, v):
                # if there is a node with two parents
                if candidate1:
                    # Return the edge with first parent
                    return candidate1
                # else return the edge causing cycle
                return [u, v]
        # this means there is a node with two parents and the first edge does not cause a cycle, hence return the second edge, becuase it must create a cycle.
        return candidate2


