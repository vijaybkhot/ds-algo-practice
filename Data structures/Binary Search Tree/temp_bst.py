class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_iterative(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return self.root

        current = self.root
        while current:
            if value < current.value:
                if current.left is None:
                    current.left = node
                    node.parent = current
                    return self.root
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = node
                    node.parent = current
                    return self.root
                else:
                    current = current.right
            else:
                print('The value already exists inside the tree. Cannot insert duplicate values.')
                return self.root

    def search_recursive(self, node, value):
        if node is None:
            return None
        if value < node.value:
            return self.search_recursive(node.left, value)
        elif value > node.value:
            return self.search_recursive(node.right, value)
        else:
            return node

    def search_recursive_wrapper(self, value):
        return self.search_recursive(self.root, value)

    def search_iterative(self, value):
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current
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

    def inOrderTraversal(self, node):
        if node is not None:
            self.inOrderTraversal(node.left)
            print(node.value)
            self.inOrderTraversal(node.right)

    def inOrderTraversalWrapper(self):
        self.inOrderTraversal(self.root)

    def preOrderTraversal(self, node):
        if node is not None:
            print(node.value)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def preOrderTraversalWrapper(self):
        self.preOrderTraversal(self.root)

    def postOrderTraversal(self, node):
        if node is not None:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node.value)

    def postOrderTraversalWrapper(self):
        self.postOrderTraversal(self.root)

    def inOrderSuccessor(self, value):
        node = self.search_recursive_wrapper(value)
        if node is None:
            return None
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current.value
        # Node does not have a right subtree
        # Start from the root node
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

    def inOrderSuccessorParentNode(self, value):
        node = self.search_recursive_wrapper(value)
        if node is None:
            return None
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current.value
        # No right subtree
        x = node
        y = node.parent
        while y is not None and x != y.left:
            x = y
            y = y.parent
        if y is not None:
            return y.value
        else:
            return None

    def inOrderPredecessorParentNode(self, value):
        node = self.search_recursive_wrapper(value)
        if node is None:
            return None
        if node.left:
            current = node.left
            while current.right:
                current = current.right
            return current.value

        parent = node.parent
        while parent is not None and node == parent.left:
            node = parent
            parent = parent.parent
        if parent is not None:
            return parent.value
        else:
            return None

    def inOrderPredecessor(self, value):
        node = self.search_recursive_wrapper(value)
        if node is None:
            return None
        if node.left:
            current = node.left
            while current.right:
                current = current.right
            return current.value
        ancestor = self.root
        predecessor = None
        while ancestor != node:
            if value > ancestor.value:
                predecessor = ancestor
                ancestor = ancestor.right
            else:
                ancestor = ancestor.left
        if predecessor:
            return predecessor.value
        else:
            return None

    def deleteNode(self, node, value):
        # Base case: if the node is None, return None
        if node is None:
            return None

        # If the value to be deleted is less than the node's value, recur on the left subtree
        if value < node.value:
            node.left = self.deleteNode(node.left, value)

        # If the value to be deleted is greater than the node's value, recur on the right subtree
        elif value > node.value:
            node.right = self.deleteNode(node.right, value)

        # Node to be deleted is found
        else:
            # Case 1: Node has no children (it's a leaf node)
            if node.right is None and node.left is None:
                return None

            # Case 2: Node has only one child (left child)
            elif node.right is None:
                return node.left

            # Case 3: Node has only one child (right child)
            elif node.left is None:
                return node.right

            # Case 4: Node has two children
            # Find the in-order successor (minimum value in the right subtree)
            current = node.right
            while current.left:
                current = current.left

            # Replace node's value with the in-order successor's value
            node.value = current.value

            # Delete the in-order successor
            node.right = self.deleteNode(node.right, current.value)

        # Return the (possibly new) root of the subtree
        return node

    def deleteNodeWrapper(self, value):
        self.deleteNode(self.root, value)


