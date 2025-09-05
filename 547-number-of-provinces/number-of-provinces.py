class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        n = len(isConnected)

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    graph[i].add(j)
        
        visited = set()
        # def dfs(node):
        #     if node in visited:
        #         return
        #     visited.add(node)
        #     for nei in graph[node]:
        #         if nei not in visited:
        #             dfs(nei)

        # def dfs(i):
        #     for j in range(n):
        #         if isConnected[i][j] == 1 and j not in visited:
        #             visited.add(j)
        #             dfs(j)

        def bfs(node):
            q = deque()
            q.append(node)
            
            while q:
                curr = q.popleft()
                for j in range(n):
                    if isConnected[curr][j] == 1 and j not in visited:
                        visited.add(j)
                        q.append(j)
            

                
        num_components = 0

        for i in range(n):
            if i not in visited:
                num_components += 1
                visited.add(i)
                bfs(i)

        return num_components
        

