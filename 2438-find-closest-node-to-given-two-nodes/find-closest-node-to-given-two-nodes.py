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
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # q = deque()
        # q.append(node1)
        # q.append(node2)
        # answer_set = set()

        # uf = UnionFind()
        # for i in range(len(edges)):
        #     uf.find(i)
        # for u, v in enumerate(edges):
        #     if v != -1:
        #         uf.union(u, v)

        # if uf.find(node1) != uf.find(node2):
        #     return -1

        # while q:
        #     curr_node = q.popleft()
        #     if curr_node in answer_set:
        #         return curr_node
        #     answer_set.add(curr_node)
        #     if edges[curr_node] != -1:
        #         q.append(edges[curr_node])
        
        # return -1

        distance_1 = {}
        distance_2 = {}

        count1, count2 = 0, 0
        q1, q2 = deque(), deque()
        visited_1, visited_2 = set(), set()
        q1.append(node1)
        visited_1.add(node1)
        q2.append(node2)
        visited_2.add(node2)
        while q1:
            curr = q1.popleft()
            distance_1[curr] = count1
            count1 += 1
            if edges[curr] != -1 and edges[curr] not in visited_1:
                q1.append(edges[curr])
                visited_1.add(edges[curr])
                

        
        while q2:
            curr = q2.popleft()
            distance_2[curr] = count2
            count2 += 1
            if edges[curr] != -1 and edges[curr] not in visited_2:
                q2.append(edges[curr])
                visited_2.add(edges[curr])
        
        max_dist = {}
        for node in distance_1:
            if node in distance_2:
                max_dist[node] = (max(distance_1[node], distance_2[node]), node)
        
        if not max_dist:
            return -1

        _, answer_node = min(max_dist.values())
        return answer_node

        