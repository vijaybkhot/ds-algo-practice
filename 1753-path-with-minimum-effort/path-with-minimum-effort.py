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
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootY] < self.rank[rootX]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
        
        return True

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        # q = deque()
        # q.append((rows-1, cols-1, 0, set()))
        # path = []
        # path.append(heights[rows-1][cols-1])
        # visited.add((rows-1,cols-1))
        # max_diff = 0

        # while q:
        #     row, col, path_max, path = q.popleft()
        #     if row == 0 and col == 0:
        #         break
        #     for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        #         r, c = row + dr, col + dc
        #         if 0 <= r < rows and 0 <= c < cols and (r, c) not in path:
        #             q.append()
                    
        #     q.append(curr_min[1])
        #     path.append(curr_min[0])
        #     visited.add(curr_min[1])
        
        # # Calculate max difference
        # if len(path) <= 1:
        #     return 0
        # max_diff = float('-inf')
        # for i in range(1, len(path)):
        #     max_diff = max(abs(path[i]-path[i-1]), max_diff)
        
        # return path

        # # Using Kruskals algo:
        # graph = defaultdict(set)
        # edges_heap = []
        # uf = UnionFind()
        # for row in range(rows):
        #     for col in range(cols):
        #         for dr, dc in [(1, 0), (0, 1)]:
        #             r = row+dr
        #             c = col+dc
        #             if 0 <= r < rows and 0 <= c < cols:
        #                 heapq.heappush(edges_heap, (abs(heights[row][col]-heights[r][c]), (row, col), (r, c)))
        
        # max_weight = 0
        # while edges_heap:
        #     weight, u, v = heapq.heappop(edges_heap)
        #     isUnion = uf.union(u, v)
        #     if not isUnion:
        #         continue
        #     max_weight = max(max_weight, weight)
        #     rootX = uf.find((0, 0))
        #     rootY = uf.find((rows-1, cols-1))
        #     if rootX == rootY:
        #         break
            
        # return max_weight

        # Using Kruskals algo:
        graph = defaultdict(set)
        edges_heap = []
        uf = UnionFind()
        for row in range(rows):
            for col in range(cols):
                for dr, dc in [(1, 0), (0, 1)]:
                    r = row+dr
                    c = col+dc
                    if 0 <= r < rows and 0 <= c < cols:
                        edges_heap.append((abs(heights[row][col]-heights[r][c]), (row, col), (r, c)))
        heapq.heapify(edges_heap)
        max_weight = 0
        while edges_heap:
            weight, u, v = heapq.heappop(edges_heap)
            isUnion = uf.union(u, v)
            if not isUnion:
                continue
            max_weight = max(max_weight, weight)
            rootX = uf.find((0, 0))
            rootY = uf.find((rows-1, cols-1))
            if rootX == rootY:
                break
            
        return max_weight
            

            


                        




        