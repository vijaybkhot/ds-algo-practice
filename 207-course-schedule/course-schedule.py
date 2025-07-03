class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
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
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
        return True



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a graph
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        topo = 0
        
       
        while queue:
            curr_node = queue.popleft()
            topo += 1

            for nei in graph[curr_node]:
                indegree[nei] -= 1
                if indegree[nei]==0:
                    queue.append(nei)
        
        return topo == numCourses







        # # Create a graph:
        # graph = defaultdict(set)
        # indegree = defaultdict(int)

        # for v, u in prerequisites:
        #     graph[u].add(v)
        #     indegree[v] += 1

        # # # Union Find: Cycle detection for undirected graphs
        # # uf = UnionFind()
        
        # # for u in graph:
        # #     for v in graph[u]:
        # #         if not uf.union(u, v):
        # #             return False
        # # return True


        # # # DFS Cycle detection - Boolean List
        # # rec_stack = [False]*numCourses
        # # visited = [False]*numCourses
        # # def dfs(node):
        # #     visited[node] = True
        # #     rec_stack[node] = True
        # #     for nei in graph[node]:
        # #         if rec_stack[nei]:
        # #             return False
        # #         if not visited[nei]:
        # #             if not dfs(nei):
        # #                 return False
        # #     rec_stack[node] = False
        # #     return True

        # # visited = set()
        # # rec_stack = set()

        # # def dfs(node):
        # #     visited.add(node)
        # #     rec_stack.add(node)
            
        # #     for nei in graph[node]:
        # #         if nei in rec_stack:
        # #             return False
        # #         if nei not in visited:
        # #             if not dfs(nei):
        # #                 return False

        # #     rec_stack.remove(node)
        # #     return True


        # # Color Node:
        # color = ['white']*numCourses
        # def dfs(node):
        #     color[node] = 'grey'

        #     for nei in graph[node]:
        #         if color[nei] == 'grey':
        #             return False
        #         if color[nei] == 'white':
        #             if not dfs(nei):
        #                 return False

        #     color[node] = 'black'
        #     return True


        
        # for i in range(numCourses):
        #     if color[i] == 'white':
        #         if not dfs(i):
        #             return False
        
        # return True
        


        
        # # # Kahn's BSF algorithm to detect a cycle
        # # q = deque()
        # # total = numCourses

        # # # start with 0 indegree
        # # for u in range(numCourses):
        # #     if indegree[u] == 0:
        # #         q.append(u)
        # #         total -= 1
        
        # # while q:
        # #     curr_node = q.popleft()
        # #     for nei in graph[curr_node]:
        # #         indegree[nei] -= 1
        # #         if indegree[nei] == 0:
        # #             del indegree[nei]
        # #             q.append(nei)
        # #             total -= 1
        
        # # return total==0


        # # # Create graph
        # # graph = defaultdict(set)
        # # inDegree = [0] * numCourses
        # # for a, b in prerequisites:
        # #     graph[b].add(a)
        # #     inDegree[a] += 1

        # # # visited = [False] * numCourses
        # # # rec_stack = [False] * numCourses

        # # # def dfs(node):
        # # #     visited[node] = True
        # # #     rec_stack[node] = True

        # # #     for neighbor in graph[node]:
        # # #         if not visited[neighbor]:
        # # #             if dfs(neighbor):
        # # #                 return True
        # # #         elif rec_stack[neighbor]:
        # # #             return True
        # # #     rec_stack[node] = False
        # # #     return False
        
        # # # for node in range(numCourses):
        # # #     if not visited[node]:
        # # #         if dfs(node):
        # # #             return False
        # # # return True

        # # queue = deque()

        # # for i in range(numCourses):
        # #     if inDegree[i] == 0:
        # #         queue.append(i)
        # # topo_order = []
        # # while queue:
        # #     node = queue.popleft()
        # #     topo_order.append(node)

        # #     for neighbor in graph[node]:
        # #         inDegree[neighbor] -= 1
        # #         if inDegree[neighbor] == 0:
        # #             queue.append(neighbor)
        
        # # return len(topo_order) == numCourses

