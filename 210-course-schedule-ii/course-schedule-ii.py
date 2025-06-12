class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegree = defaultdict(int)

        for v, u in prerequisites:
            graph[u].add(v)
            indegree[v] += 1
        # DFS approach with cycle detection:
        visited = set()
        rev_topo = []
        recursion_stack = [False]*numCourses
        visited = [False]*numCourses
        def dfs(node):
            recursion_stack[node] = True
            nonlocal rev_topo
            for nei in graph[node]:
                if recursion_stack[nei]:
                    return False
                if not visited[nei]:
                    visited[nei] = True
                    if not dfs(nei):
                        return False

            rev_topo.append(node)
            recursion_stack[node] = False
            return True
        
        for i in range(numCourses):
            if not visited[i]:
                visited[i] = True
                if not dfs(i):
                    return []
        
        return rev_topo[::-1]



        ## Kahns Algorithm
        # topo = []
        # q = deque()
        # # start with 0 indegree nodes
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         q.append(i)
        
        # while q:
        #     curr_node = q.popleft()
        #     topo.append(curr_node)
        #     for nei in graph[curr_node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             q.append(nei)
        
        # return [] if len(topo)!= numCourses else topo











        # # # Topological sorting using Kahn's algorithm
        # graph = defaultdict(set)
        # in_degree = [0] * numCourses
        # for a, b in prerequisites:
        #     graph[b].add(a)
        #     in_degree[a] += 1
        
        # queue = deque()

        # for i in range(numCourses):
        #     if in_degree[i] == 0:
        #         queue.append(i)
        
        # topo_order = []

        # while queue:
        #     node = queue.popleft()
        #     topo_order.append(node)

        #     for neighbor in graph[node]:
        #         in_degree[neighbor] -= 1
        #         if in_degree[neighbor] == 0:
        #             queue.append(neighbor)
        
        # return topo_order if len(topo_order) == numCourses else []

        # # Topological sorting using DFS
        # visited = set()
        # rec_stack = set()
        # hasCycle = False
        # topo_order = []
        # def dfs(node):
        #     nonlocal hasCycle
        #     nonlocal topo_order
        #     if not hasCycle:
        #         visited.add(node)
        #         rec_stack.add(node)
        #         for neighbor in graph[node]:
        #             if neighbor not in visited:
        #                 dfs(neighbor)
        #             elif neighbor in rec_stack:
        #                 topo_order = []
        #                 hasCycle = True
        #                 return
        #         if not hasCycle:
        #             topo_order.append(node)
        #             rec_stack.remove(node)

        # for node in range(numCourses):
        #     if node not in visited:
        #         dfs(node)
        
        # return topo_order[::-1] if topo_order else []