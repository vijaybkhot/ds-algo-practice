class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0]*n
        res = []
        def dfs(node):
            if state[node] != 0:
                return state[node] == 2
            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            state[node] = 2
            return True
        
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res
            