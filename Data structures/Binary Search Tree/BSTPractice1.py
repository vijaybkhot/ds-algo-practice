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
                    print("The value already exists inside the BST. Cannot insert duplicate values.")
                    return self.root

    def insert_iterative_1(self, value):
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
                    print("The value already exists inside the BST. Cannot insert duplicate values.")
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

    def search_1(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete_node(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete_node(node.left, value)
        elif value > node.value:
            node.right = self.delete_node(node.right, value)
        else:
            # Node to delete found
            # For node with no children
            if node.left is None and node.right is None:
                return None
            # For node with one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # The node has both left and right children
            else:
                # Find the minimum in right subtree
                current = node.right
                while current.left:
                    current = current.left
                # Replace the nodes value with the minimum value in right subtree
                node.value = current.value
                # Delete the node with the minimum value in the right subtree
                node.right = self.delete_node(node.right, current.value)
        return node

    def delete_node_wrapper(self, value):
        self.root = self.delete_node(self.root, value)
        return self.root

    def delete_node_1(self, node, value):
        if node is None:
            return None
        else:
            if value < node.value:
                node.left = self.delete_node_1(node.left, value)
            elif value > node.value:
                node.right = self.delete_node_1(node.right, value)
            else:
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    current = node.right
                    while current.left:
                        current = current.left
                    node.value = current.value
                    node.right = self.delete_node_1(node.right, current.value)
            return node

    def delete_node_wrapper_1(self, value):
        self.root = self.delete_node_1(self.root, value)
        return self.root

    def inorder_walk(self, node):
        if node is not None:
            self.inorder_walk(node.left)
            print(node.value)
            self.inorder_walk(node.right)

    def inorder_walk_wrapper(self):
        self.inorder_walk(self.root)

    def inorder_walk_1(self, node):
        if node is not None:
            self.inorder_walk_1(node.left)
            print(node.value)
            self.inorder_walk_1(node.right)

    def inorder_walk_wrapper_1(self):
        self.inorder_walk_1(self.root)

    def inorder_successor(self, value):
        # Find the node in the Tree
        node = self.search(value)
        # If the node is not present in the tree, there is no successor
        if node is None:
            return None

        # If the node is found, check if it has a right subtree
        # If the node has a right subtree, the successor is the minimum element in the right subtree
        if node.right is not None:
            current = node.right
            while current.left:
                current = current.left
            return current.value
        else:
            # There is no right subtree, we find the closest ancestor of our main node whose left subtree contains
            # our node
            ancestor = self.root
            successor = None
            while ancestor != node:
                if node.value < ancestor.value:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            if successor is not None:
                return successor.value
            else:
                return None

    def inorder_successor_1(self, value):
        node = self.search(value)
        if node is None:
            return None
        else:
            # Node is found
            if node.right is not None:
                current = node.right
                while current.left:
                    current = current.left
                return current.value
            else:
                # Node does not have a right subtree
                ancestor = self.root
                successor = None
                while ancestor != node:
                    if value < ancestor.value:
                        successor = ancestor
                        ancestor = ancestor.left
                    else:
                        ancestor = ancestor.right
                if successor is not None:
                    return successor.value
                else:
                    return None

    def tree_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def tree_max(self):
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

# Test inorder successor for nodes with right subtree
assert bst.inorder_successor_1(3) == 4  # Successor of 3 is 4
assert bst.inorder_successor_1(5) == 6  # Successor of 5 is 6
assert bst.inorder_successor_1(7) == 8  # Successor of 7 is 8

# Test inorder successor for nodes without right subtree
assert bst.inorder_successor_1(2) == 3  # Successor of 2 is 3
assert bst.inorder_successor_1(4) == 5  # Successor of 4 is 5
assert bst.inorder_successor_1(6) == 7  # Successor of 6 is 7
assert bst.inorder_successor_1(8) is None  # Successor of 8 is None (no successor)

print("All test cases passed.")









