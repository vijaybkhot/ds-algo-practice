from sortedcontainers import SortedSet

class UnionFind:
    def __init__(self):
        self.connections = {}
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            if self.rank[pu] == self.rank[pv]:
                self.rank[pu] += 1
    
    def remove(self, x):
        self.rank[x] = None
        del self.parent[x]



class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # component_map = defaultdict(SortedSet)
        # node_component_map = defaultdict(int)
        # curr_component = 1

        # graph = defaultdict(set)
        # for u, v in connections:
        #     graph[u].add(v)
        #     graph[v].add(u)
        
        # visited = set()
        # def dfs(node, curr_component):
        #     if node in visited:
        #         return
        #     visited.add(node)
        #     component_map[curr_component].add(node)
        #     node_component_map[node] = curr_component
        #     for nei in graph[node]:
        #         dfs(nei, curr_component)

            
        # for node in range(1, c+1):
        #     if node not in visited:
        #         dfs(node, curr_component)
        #         curr_component += 1
        
        # res = []

        # for query_type, node in queries:
        #     # get the component for the node
        #     component = node_component_map[node]
        #     if query_type == 1:
        #         # check if the node is present in the component map
        #         if node in component_map[component]:
        #             res.append(node)
        #         else:
        #             if component_map[component]:
        #                 res.append(component_map[component][0])
        #             else:
        #                 res.append(-1)
        #     else:
        #         if node in component_map[component]:
        #             component_map[component].remove(node)
        
        # return res

        # Using Disjoint Union Set
        res = []
        uf = UnionFind()
        for u, v in connections:
            uf.union(u, v)
        
        component_map = defaultdict(SortedSet)

        for node in range(1, c+1):
            root_c = uf.find(node)
            component_map[root_c].add(node)
        
        for query_type, node in queries:
            # get the root for the node
            root_node = uf.find(node)
            if query_type == 1:
                # check if the node is present in the component map
                if node in component_map[root_node]:
                    res.append(node)
                else:
                    if component_map[root_node]:
                        res.append(component_map[root_node][0])
                    else:
                        res.append(-1)
            else:
                if node in component_map[root_node]:
                    component_map[root_node].remove(node)
        
        return res

            
                


        
        