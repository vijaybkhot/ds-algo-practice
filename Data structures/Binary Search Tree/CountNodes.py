"""
Space complexity: worst case height of binary tree. O(n)
Time complexity: O(n). Because we are visiting all the nodes once
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def countNodes(root):
    if root is None:
        return 0
    leftCount = countNodes(root.left)
    rightCount = countNodes(root.right)
    return leftCount + rightCount + 1


def countNode1(root):
    if root is None:
        return 0
    leftCount = countNode1(root.left)
    rightCount = countNode1(root.right)
    return leftCount + rightCount + 1


def countNode2(root):
    if root is None:
        return 0
    leftCount = countNode2(root.left)
    rightCount = countNode2(root.right)
    return leftCount + rightCount + 1




# Example Usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Count the nodes in the tree
print(countNodes(root))  # Output: 7
