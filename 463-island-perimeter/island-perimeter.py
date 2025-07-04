class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                    return 1
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))
        
            return dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
        
        start_r, start_c = 0, 0
        for i in range(rows):
            if grid[start_r][start_c] != 1:
                for j in range(cols):
                    if grid[i][j] == 1:
                        start_r, start_c = i, j
                        break
            else:
                break


        return dfs(start_r, start_c)




















#         # # Brute force solution
#         # res = 0
#         # for i in range(len(grid)):
#         #     for j in range(len(grid[0])):
#         #         if grid[i][j] == 1:
#         #             isLeft = grid[i][j-1] if j-1 > -1 else 0
#         #             isRight = grid[i][j+1] if j+1 < len(grid[0]) else 0
#         #             isTop = grid[i-1][j] if i-1 > -1 else 0
#         #             isBottom = grid[i+1][j] if i+1 < len(grid) else 0
#         #             isLeft = 1 if not isLeft else 0
#         #             isRight = 1 if not isRight else 0
#         #             isTop = 1 if not isTop else 0
#         #             isBottom = 1 if not isBottom else 0
#         #             res += (isLeft + isRight + isTop + isBottom)

#         # return res
        
#         # DFS Solution
#         # visited = set()

#         # def dfs(i, j):
#         #     if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
#         #         return 1
#         #     if (i, j) in visited:
#         #         return 0
        
#         #     visited.add((i, j))
            
#         #     return dfs(i, j-1) + dfs(i, j+1) + dfs(i-1, j) + dfs(i+1, j)
        
#         # i, j = 0, 0
#         # for r in range(len(grid)):
#         #     if i and j:
#         #         break
#         #     for c in range(len(grid[0])):
#         #         if grid[r][c] == 1:
#         #             i = r
#         #             j = c
#         #             break
        
#         # return dfs(i, j)

#         visited = set()
#         self.res = 0
#         # BFS Solution:
#         def bfs(i, j):
#             q = deque([(i, j)])
#             visited.add((i, j))
#             while q:
#                 r, c = q.popleft()
#                 left, right, top, bottom = 1, 1, 1, 1
#                 if c == 0 or grid[r][c-1]==0:
#                     self.res += 1
#                     left = None
#                 if c == len(grid[0])-1 or grid[r][c+1]==0:
#                     self.res += 1
#                     right = None
#                 if r == 0 or grid[r-1][c] == 0:
#                     self.res += 1
#                     top = None
#                 if r == len(grid) - 1 or grid[r+1][c] == 0:
#                     self.res += 1
#                     bottom = None

                    
#                 if left and (r, c-1) not in visited:
#                     q.append((r, c-1))
#                     visited.add((r, c-1))
#                 if right and (r, c+1) not in visited:
#                     q.append((r, c+1))
#                     visited.add((r, c+1))
#                 if top and (r-1, c) not in visited:
#                     q.append((r-1, c))
#                     visited.add((r-1, c))
#                 if bottom and (r+1, c) not in visited:
#                     q.append((r+1, c))
#                     visited.add((r+1, c))
        
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == 1:
#                     bfs(r, c)
#                     return self.res
        
                
                

                
                
        
        