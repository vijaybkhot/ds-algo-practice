class UnionFind:
    def __init__(self, size):
        self.parent = [-1]*(size+1)
    
    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        
        if self.parent[rootX] < self.parent[rootY]:
            self.parent[rootX] += self.parent[rootY]
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] += self.parent[rootX]
            self.parent[rootX] = rootY
        return True


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # # DFS Approach:
        # graph = defaultdict(set)
        # visited = set()
        # for u, v in edges:
        #     graph[u].add(v)
        #     graph[v].add(u)

        # def dfs(node):
        #     if node in visited:
        #         return
        #     if node == destination:
        #         return True
        #     visited.add(node)
        #     for nei in graph[node]:
        #         if nei not in visited:
        #             if dfs(nei):
        #                 return True
        #     return False

        # return dfs(source)

        # Union Find approach:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        
        return not uf.union(source, destination)

        