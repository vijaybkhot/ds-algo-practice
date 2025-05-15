class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

#         def Kruskals(edge_list, n, forced_edge_idx=None, excluded_edge_idx=None):
#             uf = UnionFind(n)
#             mst_weight = 0
#             count = 0

#             if forced_edge_idx is not None:
#                 u, v, w, _ = edge_list[forced_edge_idx]
#                 if uf.union(u, v):
#                     mst_weight += w
#                     count += 1
            
#             for i, (u, v, w, _) in enumerate(edge_list):
#                 if i == forced_edge_idx or i == excluded_edge_idx:
#                     continue
#                 if uf.union(u, v):
#                     mst_weight += w
#                     count += 1
            
#             return (count == n - 1), mst_weight 
            
#         edges_with_idx = [[u, v, w, i] for i, (u, v, w) in enumerate(edges)]
#         edges_with_idx.sort(key=lambda x: x[2])

#         is_valid, min_mst_weight = Kruskals(edges_with_idx, n)

#         if not is_valid:
#             return [[], []]
#         critical = []
#         psuedo = []

#         for i in range(len(edges_with_idx)):
#             # Check if edge is critical
#             is_valid, weight = Kruskals(edges_with_idx, n, excluded_edge_idx=i)
#             if not is_valid or weight > min_mst_weight:
#                 critical.append(edges_with_idx[i][3])
#             else:
#                 # Check if edge is psuedo critical
#                 is_valid, weight = Kruskals(edges_with_idx, n, forced_edge_idx=i)
#                 if is_valid and weight == min_mst_weight:
#                     psuedo.append(edges_with_idx[i][3])
        
#         return [critical, psuedo]



# class UnionFind:
#     def __init__(self, size):
#         self.parent = [-1] * size
    
#     def find(self, x):
#         if self.parent[x] < 0:
#             return x
#         self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
    
#     def union(self, x, y):
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX == rootY:
#             return False
#         if self.parent[rootX] > self.parent[rootY]:
#             rootX, rootY = rootY, rootX
#         self.parent[rootX] += self.parent[rootY]
#         self.parent[rootY] = rootX
#         return True




        def Kruskals(edgeList, n, forced_edge_idx=None, excluded_edge_idx=None):
            uf = UnionFind()
            mst_weight = 0
            count = 0  # Number of edges added

            # for i in range(n):
            #     uf.find(i)

            if forced_edge_idx is not None:
                u, v, w, _ = edgeList[forced_edge_idx]
                if uf.union(u, v):
                    mst_weight += w
                    count += 1

            for i, (u, v, w, _) in enumerate(edgeList):
                if i == excluded_edge_idx or i == forced_edge_idx:
                    continue
                if uf.union(u, v):
                    mst_weight += w
                    count += 1

            return (count == n - 1), mst_weight

        # Add indices to edges
        edges_with_idx = [[u, v, w, i] for i, (u, v, w) in enumerate(edges)]
        edges_with_idx.sort(key=lambda x: x[2])

        is_valid, min_mst_weight = Kruskals(edges_with_idx, n)

        if not is_valid:
            return [[], []]

        critical = []
        psuedo = []

        for i in range(len(edges_with_idx)):
            # Check if edge is critical
            is_valid, weight = Kruskals(edges_with_idx, n, excluded_edge_idx=i)
            if not is_valid or weight > min_mst_weight:
                critical.append(edges_with_idx[i][3])
            else:
                # Check if edge is pseudo-critical
                is_valid, weight = Kruskals(edges_with_idx, n, forced_edge_idx=i)
                if is_valid and weight == min_mst_weight:
                    psuedo.append(edges_with_idx[i][3])

        return [critical, psuedo]



        


        
        

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1

        return True