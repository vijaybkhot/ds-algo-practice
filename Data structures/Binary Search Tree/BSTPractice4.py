class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_iterative(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return self.root
        else:
            current = self.root
            while current:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        return self.root
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = new_node
                        return self.root
                    else:
                        current = current.right
                else:
                    print("Value already exists in the BST. Cannot insert duplicate values.")
                    return self.root

    def search(self, value):
        if self.root is None:
            return None
        else:
            current = self.root
            while current:
                if value == current.value:
                    return current
                elif value < current.value:
                    current = current.left
                else:
                    current = current.right
            return None

    def delete_node(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.delete_node(node.left, value)
        elif value > node.value:
            node.right = self.delete_node(node.right, value)
        else:   # Node to be deleted found
            # If node has no children
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.right
            # Node has both left and right children
            # Find the minimum in right subtree
            current = node.right
            while current.left:
                current = current.left
            node.value = current.value
            node.right = self.delete_node(node.right, current.value)
        return node

    def delete_node_wrapper(self, value):
        self.root = self.delete_node(self.root, value)
        return self.root

    def inorder_walk(self, node):
        if node is not None:
            self.inorder_walk(node.left)
            print(node.value)
            self.inorder_walk(node.right)

    def inorder_successor(self, value):
        node = self.search(value)
        if node is None:
            return None
        else:
            if node.right:
                current = node.right
                while current.left:
                    current = current.left
                return current.value
            ancestor = self.root
            successor = None
            while ancestor != node:
                if value < ancestor.value:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            if successor:
                return successor.value
            else:
                return None

    def tree_min(self):
        current = self.root
        if current is not None:
            while current.left:
                current = current.left
            return current.value
        else:
            return None

    def tree_max(self):
        if self.root is None:
            return None
        else:
            current = self.root
            while current.right:
                current = current.right
            return current.value
# Create a binary search tree
bst = BinarySearchTree()
bst.insert_iterative(5)
bst.insert_iterative(3)
bst.insert_iterative(7)
bst.insert_iterative(2)
bst.insert_iterative(4)
bst.insert_iterative(6)
bst.insert_iterative(8)

# Test insert_iterative
assert bst.root.value == 5
assert bst.root.left.value == 3
assert bst.root.right.value == 7
assert bst.root.left.left.value == 2
assert bst.root.left.right.value == 4
assert bst.root.right.left.value == 6
assert bst.root.right.right.value == 8

# Test search
assert bst.search(5).value == 5
assert bst.search(10) == None

# Test delete_node
print(bst.search(2).value)
bst.delete_node_wrapper(2)
print(bst.search(2))
assert bst.root.left.left == None
bst.delete_node_wrapper(7)
assert bst.root.right.value == 8

# Test inorder_walk
import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def capture_stdout():
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    yield sys.stdout
    sys.stdout = old_stdout

with capture_stdout() as stdout:
    bst.inorder_walk(bst.root)
output = stdout.getvalue()
assert output == "3\n4\n5\n6\n8\n"

# Test inorder_successor
assert bst.inorder_successor(3) == 4
assert bst.inorder_successor(5) == 6
print(bst.inorder_successor(7))
assert bst.inorder_successor(8) == None

print("All test cases passed.")
