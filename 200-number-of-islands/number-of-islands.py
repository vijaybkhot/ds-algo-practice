class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_islands = 0
        visited = set()

        # # DFS Sloution:
        # def dfs(i, j):
        #     visited.add((i, j))
        #     for dr, dc in directions:
        #         r, c = i+dr, j+dc
        #         if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == '1':
        #             dfs(r, c)
        # num_islands = 0
        # visited = set()

        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == '1' and (row, col) not in visited:
        #             num_islands += 1
        #             dfs(row, col)
        
        # return num_islands

        # BFS Solution:
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            while q:
                i, j = q.popleft()
                for dr, dc in directions:
                    r, c = i+dr, j+dc
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == '1':
                        q.append((r, c))
                        visited.add((r, c))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    num_islands += 1
                    bfs(row, col)
        
        return num_islands
 
            

















#         # Counting number of connected components
#         # DFS Solution:
#         visited = set()
#         def dfs(i, j):
#             if grid[i][j] == "0":
#                 return
#             visited.add((i, j))
#             top = (i-1, j) if i-1 > -1 else None
#             bottom = (i+1, j) if i+1 < len(grid) else None
#             right = (i, j+1) if j+1 < len(grid[0]) else None
#             left = (i, j-1) if j-1 > -1 else None

#             if top and top not in visited:
#                 dfs(top[0], top[1])
#             if bottom and bottom not in visited:
#                 dfs(bottom[0], bottom[1])
#             if left and left not in visited:
#                 dfs(left[0], left[1])
#             if right and right not in visited:
#                 dfs(right[0], right[1])

#         def bfs(i, j):
#             q = deque()
#             visited.add((i, j))
#             q.append((i, j))
#             while q:
#                 i, j = q.popleft()
#                 top = (i-1, j) if i-1 > -1 else None
#                 bottom = (i+1, j) if i+1 < len(grid) else None
#                 left = (i, j+1) if j+1 < len(grid[0]) else None
#                 right = (i, j-1) if j-1 > -1 else None

#                 if top and top not in visited:
#                     if grid[top[0]][top[1]] == "1":
#                         visited.add((top[0], top[1]))
#                         q.append((top[0], top[1]))
#                 if bottom and bottom not in visited:
#                     if grid[bottom[0]][bottom[1]] == "1":
#                         visited.add((bottom[0], bottom[1]))
#                         q.append((bottom[0], bottom[1]))
#                 if left and left not in visited:
#                     if grid[left[0]][left[1]] == "1":
#                         visited.add((left[0], left[1]))
#                         q.append((left[0], left[1]))
#                 if right and right not in visited:
#                     if grid[right[0]][right[1]] == "1":
#                         visited.add((right[0], right[1]))
#                         q.append((right[0], right[1]))



#         islands = 0

#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == "1" and (r, c) not in visited:
#                     islands += 1
#                     dfs(r, c)
        
#         return islands

        