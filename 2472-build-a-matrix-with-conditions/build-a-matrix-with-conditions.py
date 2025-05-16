class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        # Using topological sorting
        def topo_sort_bfs(edge_list):
            graph = defaultdict(set)
            indegree = defaultdict(int)

            for i in range(1, k+1):
                graph[i] = set()
                indegree[i] = 0
            
            for u, v in edge_list:
                if v not in graph[u]: 
                    graph[u].add(v)
                    indegree[v] += 1
                    
            q = deque([node for node in indegree if indegree[node] == 0])

            topo_order = []
            while q:
                node = q.popleft()
                topo_order.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1 
                    if indegree[nei] == 0:
                        q.append(nei)
            
            return topo_order if len(topo_order) == len(indegree) else []

        def topo_sort_dfs(edges):
            graph = defaultdict(set)
            visited = set()
            visiting = set()
            topo_order = []

            for u in range(1, k+1):
                graph[u]

            for u, v in edges:
                graph[u].add(v)

            def dfs(node):
                if node in visiting:
                    return True
                if node in visited:
                    return False
                visiting.add(node)
                for nei in graph[node]:
                    if dfs(nei):
                        return True
                visiting.remove(node)
                visited.add(node)
                topo_order.append(node)
            
            for node in range(1, k+1):
                if node not in visited:
                    if dfs(node):
                        return []
            
            return topo_order[::-1]

                    


        # row_order = topo_sort_dfs(list(set(tuple(edge) for edge in rowConditions)))
        # col_order = topo_sort_dfs(list(set(tuple(edge) for edge in colConditions)))
        row_order = topo_sort_bfs(rowConditions)
        col_order = topo_sort_bfs(colConditions)
        

        if not row_order or not col_order:
            return []
        
        row_map = {num:idx for idx, num in enumerate(row_order)}
        col_map = {num:idx for idx, num in enumerate(col_order)}

        res = [[0]*k for i in range(k)]
        
        for num in row_map:
            res[row_map[num]][col_map[num]] = num
        
        return res


