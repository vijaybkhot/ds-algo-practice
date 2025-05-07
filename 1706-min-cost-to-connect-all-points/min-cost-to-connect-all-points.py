class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = UnionFind()

        # Using Kruskal's algorithm
        # Calculate edge lengths between each nodes
        edges = []
        # for i in range(len(points)):
        #     for j in range(i+1, len(points)):
        #         u, v = points[i], points[j]
        #         dist_uv = abs(u[0] - v[0]) + abs(u[1] - v[1])
        #         edges.append((dist_uv, (u[0], u[1]), (v[0], v[1])))

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                u, v = points[i], points[j]
                dist_uv = abs(u[0] - v[0]) + abs(u[1] - v[1])
                edges.append((dist_uv, i, j))
        
        edges.sort(key=lambda x: x[0])
        res = 0

        for w, u, v in edges:
            isRootDifferent = uf.union(u, v)
            if not isRootDifferent:
                continue
            else:
                res += w
        
        return res

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        find = self.find
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if x != self.parent[x]:
            self.parent[x] = find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        find = self.find
        rootX = find(x)
        rootY = find(y)

        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
        return True

        
