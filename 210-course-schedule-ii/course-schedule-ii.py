class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological sorting using Kahn's algorithm
        graph = defaultdict(set)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].add(a)
            in_degree[a] += 1
        
        queue = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return topo_order if len(topo_order) == numCourses else []
        