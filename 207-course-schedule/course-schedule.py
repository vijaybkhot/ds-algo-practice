class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a graph:
        graph = defaultdict(set)
        indegree = defaultdict(int)

        for v, u in prerequisites:
            graph[u].add(v)
            indegree[v] += 1
        
        visited = set()
        q = deque()
        total = numCourses
        # start with 0 indegree
        for u in range(numCourses):
            if indegree[u] == 0:
                q.append(u)
                total -= 1
        
        while q:
            curr_node = q.popleft()
            for nei in graph[curr_node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    del indegree[nei]
                    q.append(nei)
                    total -= 1
        
        return total==0
















        # # Create graph
        # graph = defaultdict(set)
        # inDegree = [0] * numCourses
        # for a, b in prerequisites:
        #     graph[b].add(a)
        #     inDegree[a] += 1

        # # visited = [False] * numCourses
        # # rec_stack = [False] * numCourses

        # # def dfs(node):
        # #     visited[node] = True
        # #     rec_stack[node] = True

        # #     for neighbor in graph[node]:
        # #         if not visited[neighbor]:
        # #             if dfs(neighbor):
        # #                 return True
        # #         elif rec_stack[neighbor]:
        # #             return True
        # #     rec_stack[node] = False
        # #     return False
        
        # # for node in range(numCourses):
        # #     if not visited[node]:
        # #         if dfs(node):
        # #             return False
        # # return True

        # queue = deque()

        # for i in range(numCourses):
        #     if inDegree[i] == 0:
        #         queue.append(i)
        # topo_order = []
        # while queue:
        #     node = queue.popleft()
        #     topo_order.append(node)

        #     for neighbor in graph[node]:
        #         inDegree[neighbor] -= 1
        #         if inDegree[neighbor] == 0:
        #             queue.append(neighbor)
        
        # return len(topo_order) == numCourses

