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
                print("Value already exits in the tree. Cannot insert duplicate value")
                return self.root

    def search(self, value):
        if self.root is None:
            return None
        else:
            current = self.root
            while current:
                if value < current.value:
                    current = current.left
                elif value > current.value:
                    current = current.right
                else:
                    return current
        return None

    def delete_node(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.delete_node(node.left, value)
        elif value > node.value:
            node.right = self.delete_node(node.right, value)
        else:
            # If node to be deleted has no children
            if node.left is None and node.right is None:
                return None
            # If node has only one child, return the other child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Node has both left and right child, find the minimum in right subtree
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
            # If node has right child, find the minimum in right subtree
            if node.right is not None:
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
                if successor is not None:
                    return successor.value
                else:
                    return None

    def tree_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def tree_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current.value


# Create a Binary Search Tree
bst = BinarySearchTree()

# Test insert_iterative method
bst.insert_iterative(5)
bst.insert_iterative(3)
bst.insert_iterative(7)
bst.insert_iterative(2)
bst.insert_iterative(4)
bst.insert_iterative(6)
bst.insert_iterative(8)

# Test search method
assert bst.search(5).value == 5
assert bst.search(3).value == 3
assert bst.search(7).value == 7
assert bst.search(2).value == 2
assert bst.search(4).value == 4
assert bst.search(6).value == 6
assert bst.search(8).value == 8
assert bst.search(9) is None  # Value not in the tree

# Test inorder_successor method
assert bst.inorder_successor(2) == 3
assert bst.inorder_successor(3) == 4
assert bst.inorder_successor(4) == 5
assert bst.inorder_successor(5) == 6
assert bst.inorder_successor(6) == 7
assert bst.inorder_successor(7) == 8
assert bst.inorder_successor(8) is None  # No successor for 8

# Test delete_node_wrapper method
bst.inorder_walk(bst.root)

bst.delete_node_wrapper(3)
bst.delete_node_wrapper(7)
bst.inorder_walk(bst.root)
print("All test cases passed.")

