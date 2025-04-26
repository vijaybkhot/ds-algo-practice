class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Using Kahns algorithm:
        prereq = defaultdict(set)
        graph = defaultdict(set)
        # indegree = defaultdict(int)
        for a, b in prerequisites:
            graph[a].add(b)
            # indegree[b] += 1
        
        # q = deque()
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         q.append(i)

        # while q:
        #     node = q.popleft()
        #     for neighbor in graph[node]:
        #         prereq[neighbor].update(prereq[node])
        #         prereq[neighbor].add(node)
        #         indegree[neighbor] -= 1
        #         if indegree[neighbor] == 0:
        #             q.append(neighbor)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)
                prereq[node].add(neighbor)
                prereq[node].update(prereq[neighbor])
        
        for i in range(numCourses):
            dfs(i)

        return [True if v in prereq[u] else False for u, v in queries]
        
