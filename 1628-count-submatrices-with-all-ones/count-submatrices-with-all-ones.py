class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        # horizontal = [row[:] for row in mat]
        # vertical = [row[:] for row in mat]
        # diagonal = [row[:] for row in mat]

        # # count horizontal rectangles
        # for r in range(rows):
        #     for c in range(cols):
        #         if horizontal[r][c] == 0:
        #             continue
        #         left =  horizontal[r][c-1] if 0 <= c-1 < cols and horizontal[r][c-1] > 0 else 0
        #         horizontal[r][c] += left

        
        # # Count Verticals
        # for r in range(rows):
        #     for c in range(cols):
        #         if vertical[r][c] == 0:
        #             continue
        #         top = vertical[r-1][c] if 0 <= r-1 < rows and vertical[r-1][c] > 0 else 0
        #         vertical[r][c] += top
        
        # # Count Diagonals
        # for r in range(rows):
        #     for c in range(cols):
        #         if diagonal[r][c] == 0:
        #             continue
        #         left =  diagonal[r][c-1] if 0 <= c-1 < cols and diagonal[r][c-1] > 0 else 0
        #         top = diagonal[r-1][c] if 0 <= r-1 < rows and diagonal[r-1][c] > 0 else 0
        #         diag = diagonal[r-1][c-1] if 0 <= r-1 < rows and 0 <= c-1 < cols and diagonal[r-1][c-1] > 0 else 0
        #         if left and top and diag:
        #             while left > 0 or top > 0 or diag > 0:
        #                 diagonal[r][c] += 1
        #                 left -= 1
        #                 top -= 1
        #                 diag -= 1

        # # Count total from all
        # total = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         if mat[r][c] == 0:
        #             continue
        #         mat[r][c] = horizontal[r][c] + vertical[r][c]-1 + diagonal[r][c]-1
        #         total += mat[r][c]
        
        # return total

        # # Precompute horizontal consecutive 1s
        # horizontal = [[0] * cols for _ in range(rows)]
        # for r in range(rows):
        #     for c in range(cols):
        #         if mat[r][c] == 1:
        #             horizontal[r][c] = horizontal[r][c - 1] + 1 if c > 0 else 1

        # total = 0
        # # For each cell, look upward and count submatrices ending at (r, c)
        # for r in range(rows):
        #     for c in range(cols):
        #         if mat[r][c] == 0:
        #             continue
        #         width = horizontal[r][c]
        #         # Expand upwards
        #         for k in range(r, -1, -1):
        #             width = min(width, horizontal[k][c])
        #             if width == 0:
        #                 break
        #             total += width

        # return total

        m = len(mat)
        n = len(mat[0])
        histogram = [0] * n
        count = 0

        for i in range(m):
            # update histogram for row i
            for j in range(n):
                histogram[j] = histogram[j] + 1 if mat[i][j] == 1 else 0

            # stack of tuples (height, index, prev_count); start with sentinel
            stack = [(-1, -1, 0)]
            for j in range(n):
                while stack and stack[-1][0] >= histogram[j]:
                    stack.pop()
                prev_h, prev_idx, prev_count = stack[-1]
                curr_count = histogram[j] * (j - prev_idx) + prev_count
                stack.append((histogram[j], j, curr_count))
                count += curr_count

        return count

        # [[0,  1,  2,  0],
        # [0,   1,  2,  3],
        # [1,   2,  3,  0]]

        # [[0,  1,  1,  0],
        # [0,   2,  2,  1],
        # [1,   3,  3,  0]]

        # [[0,  1,  1,  0],
        # [1,   1,  2,  1],
        # [1,   2,  1,  0]]