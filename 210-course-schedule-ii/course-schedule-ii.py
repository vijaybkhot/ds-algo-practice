class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(set)
        for u, v in prerequisites:
            graph[v].add(u)
            indegree[u] += 1
        
        res = []
        visited = set()
        stack = set()
        def dfs(node):
            if node in stack:
                return False
            if node in visited:
                return True
            stack.add(node)
            for nei in graph[node]:
                if nei not in visited and not dfs(nei):
                    return False
            
            stack.remove(node)
            visited.add(node)
            res.append(node)
            return True

        for i in range(numCourses):
            if i not in visited and not dfs(i):
                return []
        
        return res[::-1]

        # q = deque()
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         q.append(i)
        
        # res = []
        # while q:
        #     node = q.popleft()
        #     res.append(node)
        #     for nei in graph[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             q.append(nei)
        
        # for i in range(numCourses):
        #     if indegree[i] > 0:
        #         return []
        
        # return res