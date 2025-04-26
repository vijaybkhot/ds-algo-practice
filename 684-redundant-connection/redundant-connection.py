class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # # Brute force - Try removing each edge in reverse order, and return the first edge whose removal leaves the graph connected (only one component).
        # input_graph = defaultdict(set)
        # for index, (u, v) in enumerate(edges):
        #     input_graph[u].add(v)
        #     input_graph[v].add(u)
            

        # def components(graph):
        #     def dfs(node):
        #         visited.add(node)
        #         for neighbor in graph[node]:
        #             if neighbor not in visited:
        #                 dfs(neighbor)

        #     visited = set()
        #     count = 0
        #     for node in graph:
        #         if node not in visited:
        #             count += 1
        #             dfs(node)
        #     return count

        # for i in range(len(edges)-1, -1, -1):
        #     u, v = edges[i]
        #     input_graph[u].remove(v)
        #     input_graph[v].remove(u)
        #     if components(input_graph) == 1:
        #         return edges[i]
        #     input_graph[u].add(v)
        #     input_graph[v].add(u)

        # Using Union Find
        self.parent = [-1] * (len(edges)+1)

        def find(x):
            if self.parent[x] < 0:
                return x
            self.parent[x] = find(self.parent[x])
            return self.parent[x]
        
        def union(u, v):
            rootU = find(u)
            rootV = find(v)
            if rootU== rootV:
                return False
            
            self.parent[rootU] = rootV
            return True



        idx = 0

        for index, (u, v) in enumerate(edges):
            notCycle = union(u, v)
            if not notCycle:
                idx = index
        
        return edges[idx]
            
                
