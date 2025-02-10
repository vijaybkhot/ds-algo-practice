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
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current
        return current

    def delete_node(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.delete_node(node.left, value)
        elif value > node.value:
            node.right = self.delete_node(node.right, value)
        else:
            # Node to be deleted found
            # If node does not have any children
            if node.left is None and node.right is None:
                return None
            # If the node has only one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # If the node has two children
            # Find the minimum node in right subtree
            current = node.right
            while current.left:
                current = current.left
            node.value = current.value
            node.right = self.delete_node(node.right, current.value)
        return node

    def delete_node_wrapper(self, value):
        self.root = self.delete_node(self.root, value)
        return self.root

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
            else:
                ancestor = self.root
                successor = None
                while ancestor != node:
                    if node.value < ancestor.value:
                        successor = ancestor
                        ancestor = ancestor.left
                    else:
                        ancestor = ancestor.right
                if successor:
                    return successor.value
                else:
                    return None

    def inorder_walk(self, node):
        if node is not None:
            self.inorder_walk(node.left)
            print(node.value)
            self.inorder_walk(node.right)

    def tree_max(self):
        if self.root is None:
            return None

        current = self.root
        while current.right:
            current = current.right
        return current.value

    def tree_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value

# Create a binary search tree
bst = BinarySearchTree()

# Insert nodes into the tree
bst.insert_iterative(5)
bst.insert_iterative(3)
bst.insert_iterative(7)
bst.insert_iterative(2)
bst.insert_iterative(4)
bst.insert_iterative(6)
bst.insert_iterative(8)

# Test successor for a node with a right subtree
assert bst.inorder_successor(3) == 4

# Test successor for a node without a right subtree
assert bst.inorder_successor(5) == 6

# Test successor for the last node in inorder traversal
assert bst.inorder_successor(8) is None

# Test successor for a node with no successor
assert bst.inorder_successor(4) == 5

print("All tests passed!")
