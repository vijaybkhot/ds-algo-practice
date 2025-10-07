class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        
        for u, v in prerequisites:
            graph[u].add(v)
        
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