class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for u, v in prerequisites:
            graph[v].add(u)

        state = [0]*numCourses

        def dfs(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            
            state[node] = 1

            for nei in graph[node]:
                if dfs(nei):
                    return True
            
            state[node] = 2
            return False
        
        for i in range(numCourses):
            if state[i] == 0:
                if dfs(i):
                    return False
        
        return True
