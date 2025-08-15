class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for i in range(len(equations)):
            u, v = equations[i]
            graph[u].append((v, values[i]))
            graph[v].append((u, 1/values[i]))
        
        res = []
        for u, v in queries:
            if u not in graph or v not in graph:
                res.append(-1)
                continue
            q = deque([(u, 1)])
            visited = set()
            found = False
            while q:
                curr_node, curr_dist = q.popleft()
                visited.add(curr_node)
                if curr_node == v:
                    found = True
                    res.append(curr_dist)
                    break
                for nxt_node, nxt_dist in graph[curr_node]:
                    if nxt_node not in visited:
                        q.append((nxt_node, curr_dist*nxt_dist))
            if not found:
                res.append(-1)
        
        return res
                

