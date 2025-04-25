class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # # Topological sorting using Kahn's algorithm
        graph = defaultdict(set)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].add(a)
            in_degree[a] += 1
        
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

        # Topological sorting using DFS
        visited = set()
        rec_stack = set()
        hasCycle = False
        topo_order = []
        def dfs(node):
            nonlocal hasCycle
            nonlocal topo_order
            if not hasCycle:
                visited.add(node)
                rec_stack.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dfs(neighbor)
                    elif neighbor in rec_stack:
                        topo_order = []
                        hasCycle = True
                        return
                if not hasCycle:
                    topo_order.append(node)
                    rec_stack.remove(node)

        for node in range(numCourses):
            if node not in visited:
                dfs(node)
        
        return topo_order[::-1] if topo_order else []