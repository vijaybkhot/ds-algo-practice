class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        # Using topological sorting
        def topo_sort(edge_list):
            graph = defaultdict(set)
            indegree = defaultdict(int)
            
            for u, v in edge_list:
                graph[u].add(v)
                indegree[v] += 1
                if u not in indegree:
                    indegree[u] = 0
            
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
        
        for i in range(1, k+1):
            if i not in row_order:
                row_order.append(i)
            if i not in col_order:
                col_order.append(i)
        
        res = [[0]*k for i in range(k)]
        for i in range(len(row_order)):
            for j in range(len(col_order)):
                if row_order[i] == col_order[j]:
                    res[i][j] = row_order[i]
        
        return res


