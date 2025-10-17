class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # graph = defaultdict(set)
        # for u, v in enumerate(edges):
        #     if v != -1:
        #         graph[u].add(v)

        state = [0]*len(edges)
        depth_map = {}
        max_len = -1

        def dfs(node, depth):
            nonlocal max_len
            state[node] = 1
            depth_map[node] = depth
            nxt = edges[node]

            if nxt != -1:
                if state[nxt] == 0:
                    dfs(nxt, depth+1)
                elif state[nxt] == 1:
                    max_len = max(max_len, depth - depth_map[nxt]+ 1)
            
            state[node] = 2
            depth_map.pop(node, None)

            
        
        for i in range(len(edges)):
            if state[i] == 0:
                dfs(i, 0)
            
        return max_len
