class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(set)
        indegree = defaultdict(int)
        index_dict = {}

        for u, v in prerequisites:
            graph[u].add(v)
            indegree[v] += 1
        
        # # Inefficient approach dfs for each query
        # def dfs(node, target):
        #     if node == target:
        #         return True
        #     visited = set()
        #     def helper_dfs(curr):
        #         visited.add(curr)
        #         for nei in graph[curr]:
        #             if nei == target:
        #                 return True
        #             if nei not in visited:
        #                 if helper_dfs(nei):
        #                     return True
        #         return False
        #     return helper_dfs(node)

        # return [dfs(u, v) for u, v in queries]
        prereq = defaultdict(set)
        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            
            for nei in graph[node]:
                dfs(nei)
                prereq[node].add(nei)
                prereq[node].update(prereq[nei])
            
        for i in range(numCourses):
            dfs(i)

        return [True if v in prereq[u] else False for u, v in queries]














        # # Using Kahns algorithm:
        # prereq = defaultdict(set)
        # graph = defaultdict(set)
        # # indegree = defaultdict(int)
        # for a, b in prerequisites:
        #     graph[a].add(b)
        #     # indegree[b] += 1
        
        # # q = deque()
        # # for i in range(numCourses):
        # #     if indegree[i] == 0:
        # #         q.append(i)

        # # while q:
        # #     node = q.popleft()
        # #     for neighbor in graph[node]:
        # #         prereq[neighbor].update(prereq[node])
        # #         prereq[neighbor].add(node)
        # #         indegree[neighbor] -= 1
        # #         if indegree[neighbor] == 0:
        # #             q.append(neighbor)

        # visited = set()

        # def dfs(node):
        #     if node in visited:
        #         return
        #     visited.add(node)

        #     for neighbor in graph[node]:
        #         dfs(neighbor)
        #         prereq[node].add(neighbor)
        #         prereq[node].update(prereq[neighbor])
        
        # for i in range(numCourses):
        #     dfs(i)

        # return [True if v in prereq[u] else False for u, v in queries]
        
