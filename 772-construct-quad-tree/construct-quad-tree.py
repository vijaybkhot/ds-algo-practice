"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # def hasSameValues(grid):
        #     first_value = grid[0][0]
        #     for i in range(len(grid)):
        #         for j in range(len(grid[0])):
        #             if grid[i][j] != first_value:
        #                 return [False, 0]
            
        #     return [True, first_value]
        
        # def divideIntoFour(matrix, root):
        #     n = len(matrix)
        #     if n > 1:
        #         if hasSameValues(matrix)[0]:
        #             return Node(grid[0][0], 1, None, None, None, None)

        #         new_len = n//2
        #         grid1 = [row[:new_len] for row in matrix[:new_len]]  # Top-left
        #         grid2 = [row[new_len:] for row in matrix[:new_len]]  # Top-right
        #         grid3 = [row[:new_len] for row in matrix[new_len:]]  # Bottom-left
        #         grid4 = [row[new_len:] for row in matrix[new_len:]]  # Bottom-right

        #         # Top-left
        #         if len(grid1) == 1 and len(grid1[0]) == 1:
        #             root.topLeft = Node(grid1[0][0], 1, None, None, None, None)
        #         else:
        #             top_left = hasSameValues(grid1)
        #             if top_left[0]:
        #                 root.topLeft = Node(top_left[1], 1, None, None, None, None)
        #             else:
        #                 root.topLeft =  divideIntoFour(grid1, Node(1, 0, None, None, None, None))

        #         # top-right
        #         if len(grid2) == 1 and len(grid2[0]) == 1:
        #             root.topRight = Node(grid2[0][0], 1, None, None, None, None)
        #         else:
        #             top_right = hasSameValues(grid2)
        #             if top_right[0]:
        #                 root.topRight = Node(top_right[1], 1, None, None, None, None)
        #             else:
        #                 root.topRight =  divideIntoFour(grid2, Node(1, 0, None, None, None, None))

        #         # bottom-left
        #         if len(grid3) == 1 and len(grid3[0])==1:
        #             root.bottomLeft = Node(grid3[0][0], 1, None, None, None, None)
        #         else:
        #             bottom_left = hasSameValues(grid3)
        #             if bottom_left[0]:
        #                 root.bottomLeft = Node(bottom_left[1], 1, None, None, None, None)
        #             else:
        #                 root.bottomLeft =  divideIntoFour(grid3, Node(1, 0, None, None, None, None))

        #         # bottom-right
        #         if len(grid4) == 1 and len(grid4[0]) == 1:
        #             root.bottomRight = Node(grid4[0][0], 1, None, None, None, None)
        #         else:
        #             bottom_right = hasSameValues(grid4)
        #             if bottom_right[0]:
        #                 root.bottomRight = Node(bottom_right[1],1, None, None, None, None)
        #             else:
        #                 root.bottomRight = divideIntoFour(grid4, Node(1, 0, None, None, None, None))
        #     elif n == 1:
        #         return Node(grid[0][0], 1, None, None, None, None)
                
        #     return root

        # if not grid:
        #     return []
        # return divideIntoFour(grid, Node(1, 0, None, None, None, None))

        # # More readable solution
        # def hasSameValues(matrix):
        #     first_value = matrix[0][0]
        #     for row in matrix:
        #         for val in row:
        #             if val != first_value:
        #                 return [False, 0]
        #     return [True, first_value]
        
        # def divideIntoFour(matrix):
        #     n = len(matrix)

        #     same, value = hasSameValues(matrix)
        #     if same:
        #         return Node(value, True, None, None, None, None)
            
        #     new_len = n // 2
        #     grid1 = [row[:new_len] for row in matrix[:new_len]]  # Top-left
        #     grid2 = [row[new_len:] for row in matrix[:new_len]]  # Top-right
        #     grid3 = [row[:new_len] for row in matrix[new_len:]]  # Bottom-left
        #     grid4 = [row[new_len:] for row in matrix[new_len:]]  # Bottom-right


        #     return Node(1, False, divideIntoFour(grid1), divideIntoFour(grid2), divideIntoFour(grid3), divideIntoFour(grid4))
        
        # return divideIntoFour(grid)

        # More optimized and more readable solution
        def hasSameValues(x1, y1, x2, y2):
            """Check if all values in the sub-grid from (x1, y1) to (x2, y2) are the same."""
            first_value = grid[x1][y1]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if grid[i][j] != first_value:
                        return False, 0
            return True, first_value

        def divideIntoFour(x1, y1, x2, y2):
            """Recursive function to construct the QuadTree efficiently."""
            
            # Call hasSameValues() ONCE per submatrix
            same, value = hasSameValues(x1, y1, x2, y2)
            if same:
                return Node(value, True, None, None, None, None)

            midX = (x1 + x2) // 2
            midY = (y1 + y2) // 2

            return Node(1, False,
                        divideIntoFour(x1, y1, midX, midY),  # Top-left
                        divideIntoFour(x1, midY, midX, y2),  # Top-right
                        divideIntoFour(midX, y1, x2, midY),  # Bottom-left
                        divideIntoFour(midX, midY, x2, y2))  # Bottom-right
        
        return divideIntoFour(0, 0, len(grid), len(grid))


                        



                