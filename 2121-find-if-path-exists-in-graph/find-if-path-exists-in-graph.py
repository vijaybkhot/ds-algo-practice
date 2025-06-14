class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(set)
        visited = set()
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(node):
            if node in visited:
                return
            if node == destination:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
            return False

        return dfs(source)

        