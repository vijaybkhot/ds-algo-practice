class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Brute Force approach - Use BFS to count height and count height for every node
        graph = defaultdict(set)
        indegree = [0] * n
        if not edges and n == 1:
            return [0]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            indegree[u] += 1
            indegree[v] += 1

        # def bfs(root):
        #     visited = set()
        #     q = deque()
        #     visited.add(root)
        #     q.append(root)
        #     height = -1
        #     while q:
        #         for _ in range(len(q)):
        #             node = q.popleft()
        #             for nei in graph[node]:
        #                 if nei not in visited:
        #                     visited.add(nei)
        #                     q.append(nei)
        #         height += 1
        #     return max(height, 0)
        # height_map = defaultdict(list)
        # min_height = 0
        # for i in range(n):
        #     height = bfs(i)
        #     height_map[height].append(i)
        #     min_height = height if min_height == 0 else min(min_height, height)
        
        # return height_map[min_height]

        # Using Kahn's algorithm by peeling of leaves 
        visited = set()
        q = deque()

        for i in range(n):
            if indegree[i] == 1:
                q.append(i)
        
        # while max(indegree) > 1:
        #     level_len = len(q)
        #     for _ in range(level_len):
        #         node = q.popleft()
        #         for nei in graph[node]:
        #             indegree[nei] -= 1
        #             if indegree[nei] == 1:
        #                 q.append(nei)

        remaining_nodes = n
        while remaining_nodes > 2:
            level_len = len(q)
            remaining_nodes -= level_len
            for _ in range(level_len):
                node = q.popleft()
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)
        
        return list(q)


        