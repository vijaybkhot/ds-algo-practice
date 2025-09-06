class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        def bfs(r, c, orig_color):
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == orig_color:
                        image[nr][nc] = color
                        q.append((nr, nc))
        
        if image[sr][sc] != color:
            orig_color = image[sr][sc]
            image[sr][sc] = color
            bfs(sr, sc, orig_color)
        
        return image
