class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in prerequisites:
            graph[v].add(u)
        
        res = []

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
            
            res.append(node)
            state[node] = 2
            return False
        
        for i in range(numCourses):
            if state[i] == 0:
                if dfs(i):
                    return []
        
        return res[::-1]