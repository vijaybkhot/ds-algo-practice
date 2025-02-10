class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sameTree(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    return node1.value == node2.value and sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right)


def sameTree1(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    return node1.value == node2.value and sameTree1(node1.left, node2.left) and sameTree1(node1.right, node2.right)


def sameTree2(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    return node1.value == node2.value and sameTree2(node1.left, node2.left) and sameTree2(node1.right, node2.right)


# Create first tree
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

# Create second tree
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

# Create a different tree
root3 = Node(1)
root3.left = Node(3)
root3.right = Node(2)

# Check if trees are the same
print(sameTree(root1, root2))  # Output: True (Both trees are identical)
print(sameTree(root1, root3))  # Output: False (Trees have different structures/values)
