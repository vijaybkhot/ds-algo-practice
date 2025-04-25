class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Create graph
        input_graph = defaultdict(set)
        for a, b in prerequisites:
            input_graph[b].add(a)

        def detect_cycle(graph):
            visited = [False] * numCourses
            rec_stack = [False] * numCourses

            def dfs(node):
                visited[node] = True
                rec_stack[node] = True

                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        if dfs(neighbor):
                            return True
                    elif rec_stack[neighbor]:
                        return True
                rec_stack[node] = False
                return False
            
            for node in range(numCourses):
                if not visited[node]:
                    if dfs(node):
                        return False
            return True

        return detect_cycle(input_graph)