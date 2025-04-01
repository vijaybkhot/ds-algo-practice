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
        def hasSameValues(grid):
            first_value = grid[0][0]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] != first_value:
                        return [False, 0]
            
            return [True, first_value]
        
        root = Node(1, 0)
        def divideIntoFour(matrix, root):
            n = len(matrix)
            if n > 1:
                if hasSameValues(matrix)[0]:
                    return Node(grid[0][0], 1, None, None, None, None)
                new_len = n//2
                grid1 = [row[:new_len] for row in matrix[:new_len]]  # Top-left
                grid2 = [row[new_len:] for row in matrix[:new_len]]  # Top-right
                grid3 = [row[:new_len] for row in matrix[new_len:]]  # Bottom-left
                grid4 = [row[new_len:] for row in matrix[new_len:]]  # Bottom-right

                # Top-left
                if len(grid1) == 1 and len(grid1[0]) == 1:
                    root.topLeft = Node(grid1[0][0], 1, None, None, None, None)
                else:
                    top_left = hasSameValues(grid1)
                    if top_left[0]:
                        root.topLeft = Node(top_left[1], 1, None, None, None, None)
                    else:
                        root.topLeft =  divideIntoFour(grid1, Node(1, 0, None, None, None, None))

                # top-right
                if len(grid2) == 1 and len(grid2[0]) == 1:
                    root.topRight = Node(grid2[0][0], 1, None, None, None, None)
                else:
                    top_right = hasSameValues(grid2)
                    if top_right[0]:
                        root.topRight = Node(top_right[1], 1, None, None, None, None)
                    else:
                        root.topRight =  divideIntoFour(grid2, Node(1, 0, None, None, None, None))

                # bottom-left
                if len(grid3) == 1 and len(grid3[0])==1:
                    root.bottomLeft = Node(grid3[0][0], 1, None, None, None, None)
                else:
                    bottom_left = hasSameValues(grid3)
                    if bottom_left[0]:
                        root.bottomLeft = Node(bottom_left[1], 1, None, None, None, None)
                    else:
                        root.bottomLeft =  divideIntoFour(grid3, Node(1, 0, None, None, None, None))

                # bottom-right
                if len(grid4) == 1 and len(grid4[0]) == 1:
                    root.bottomRight = Node(grid4[0][0], 1, None, None, None, None)
                else:
                    bottom_right = hasSameValues(grid4)
                    if bottom_right[0]:
                        root.bottomRight = Node(bottom_right[1],1, None, None, None, None)
                    else:
                        root.bottomRight = divideIntoFour(grid4, Node(1, 0, None, None, None, None))
            elif n == 1:
                return Node(grid[0][0], 1, None, None, None, None)
                
            return root

        if not grid:
            return []
        return divideIntoFour(grid, Node(1, 0, None, None, None, None))


                



        