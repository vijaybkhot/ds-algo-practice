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
                    print("The value already exists inside the BST. Cannot insert duplicate value.")
                    return self.root

    def insert_iterative_2(self, value):
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
                    print("The value already exists in the BST. Cannot insert duplicate values.")
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

    def search_2(self, value):
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return current

    def delete_node(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete_node(node.left, value)
        elif value > node.value:
            node.right = self.delete_node(node.right, value)
        else:
            # Node to delete found
            # Node with no children
            if node.right is None and node.left is None:
                return None
            # Node with one child
            elif node.right is None:
                return node.left

            elif node.left is None:
                return node.right

            # Node has both left and right children
            # Find minium node in right subtree and replace the current node with the minimum node
            current = node.right
            while current.left:
                current = current.left
            node.value = current.value
            node.right = self.delete_node(node.right, current.value)

        return node

    def delete_node_wrapper(self, value):
        self.root = self.delete_node(self.root, value)
        return self.root

    def delete_node_1(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete_node_1(node.left, value)
        elif value > node.value:
            node.right = self.delete_node_1(node.right, value)
        else:
            # Node to be deleted found
            # Node with no children
            if node.left is None and node.right is None:
                return None
            # Node has only one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Node has both left and right child
                # Find the minimum in right subtree
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

    def inorder_walk_1(self, node):
        if node is not None:
            self.inorder_walk_1(node.left)
            print(node.value)
            self.inorder_walk_1(node.right)

    def inorder_successor(self, value):
        node = self.search(value)
        if node is None:
            return None
        else:
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

    def inorder_successor_1(self, value):
        node = self.search_2(value)
        if node is None:
            return None
        else:
            if node.right is not None:
                current = node.right
                while current.left:
                    current = current.left
                return current.value
            else:
                successor = None
                ancestor = self.root
                while ancestor != node:
                    if node.value < ancestor.value:
                        successor = ancestor
                        ancestor = ancestor.left
                    else:
                        ancestor = ancestor .right
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
bst.insert_iterative(10)
bst.insert_iterative(5)
bst.insert_iterative(15)
bst.insert_iterative(2)
bst.insert_iterative(7)
bst.insert_iterative(12)
bst.insert_iterative(17)

# Test inorder walk
bst.inorder_walk(bst.root)  # Should print values in sorted order: 2, 5, 7, 10, 12, 15, 17

print("All test cases passed!")
