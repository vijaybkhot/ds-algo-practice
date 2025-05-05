class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(deque)
        for u, v in tickets:
            graph[u].append(v)

        for u in graph:
            graph[u] = deque(sorted(graph[u]))
            
        # # Partially correct approach:
        # res = ["JFK"]
        # while graph:
        #     if res[-1] not in graph:
        #         break
        #     next_dest = graph[res[-1]].popleft()
        #     if len(graph[res[-1]]) == 0:
        #         del graph[res[-1]]
        #     res.append(next_dest)

        # return res

        # Using Backtracking - Eulerian path traversal (specifically Hierholzer’s algorithm)

        res = []
        def dfs(airport):
            while graph[airport]:
                next_dst = graph[airport].popleft()
                dfs(next_dst)
            res.append(airport)
        
        dfs("JFK")
        return res[::-1]

        