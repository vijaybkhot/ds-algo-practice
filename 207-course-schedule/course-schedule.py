
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

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

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    
        indegree = defaultdict(int)
        graph = defaultdict(set)

        for u, v in prerequisites:
            graph[v].add(u)
            indegree[u] += 1
        
        # q = deque([])
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         q.append(i)

        # while q:
        #     curr_node = q.popleft()
        #     for nei in graph[curr_node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             q.append(nei)
        
        # for i in range(numCourses):
        #     if indegree[i] > 0:
        #         return False
        
        # return True

        # 1 -> 0 ->1
        # 1-> 0
        # 0, 1
        # graph = { }
        
        # stack {0}
        # vijsited = {}

        stack = set()
        visited = set()

        def dfs(node):
            if node in stack:
                return False
            if node in visited:
                return True
            stack.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if not dfs(nei):
                        return False
            visited.add(node)
            stack.remove(node)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True



