class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        # Using topological sorting
        def topo_sort(edge_list):
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
        
        row_order = topo_sort(list(set(tuple(edge) for edge in rowConditions)))
        col_order = topo_sort(list(set(tuple(edge) for edge in colConditions)))
        

        if not row_order or not col_order:
            return []
        
        row_map = {num:idx for idx, num in enumerate(row_order)}
        col_map = {num:idx for idx, num in enumerate(col_order)}

        res = [[0]*k for i in range(k)]
        
        for num in row_map:
            res[row_map[num]][col_map[num]] = num
        
        return res


