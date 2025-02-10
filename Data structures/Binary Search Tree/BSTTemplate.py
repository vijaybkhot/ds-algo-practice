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
        """
        Iteratively insert a new node with the given value into the binary search tree.

        Args:
        - value: The value to be inserted

        Returns:
        - The root of the modified binary search tree
        """
        # Create a new node with the given value
        new_node = Node(value)

        # If the tree is empty, set the new node as the root and return
        if self.root is None:
            self.root = new_node
            return self.root
        else:
            # Start from the root
            current = self.root
            while current:
                # If the value is less than the current node's value, move to the left child
                if value < current.value:
                    if current.left is None:
                        # If the left child is None, insert the new node as the left child
                        current.left = new_node
                        new_node.parent = current
                        return self.root  # Return the root of the modified tree
                    else:
                        # Move to the left child
                        current = current.left
                # If the value is greater than the current node's value, move to the right child
                elif value > current.value:
                    if current.right is None:
                        # If the right child is None, insert the new node as the right child
                        current.right = new_node
                        new_node.parent = current
                        return self.root  # Return the root of the modified tree
                    else:
                        # Move to the right child
                        current = current.right
                # If the value already exists in the tree, print a message and return the root
                else:
                    print("The value already exists in the BST. Cannot insert duplicate values")
                    return self.root

    def search_recursive(self, node, value):
        """
        Recursively search for a node with the given value starting from the given node.

        Args:
        - node: The current node being checked
        - value: The value being searched for

        Returns:
        - The node with the given value if found, otherwise None
        """
        # If the node is None or the value is None, return None
        if node is None or value is None:
            return None
        # If the value matches the current node's value, return the node
        elif node.value == value:
            return node
        # If the value is less than the current node's value, search in the left subtree
        elif value < node.value:
            return self.search_recursive(node.left, value)
        # If the value is greater than the current node's value, search in the right subtree
        else:
            return self.search_recursive(node.right, value)

    def search(self, value):
        """
        Search for a node with the given value in the binary search tree.

        Args:
        - value: The value being searched for

        Returns:
        - The node with the given value if found, otherwise None
        """
        # Start the search from the root node
        return self.search_recursive(self.root, value)

    def tree_min(self):
        """
        Finds and returns the node with the minimum value in the binary search tree.
        """
        current = self.root
        while current.left:
            current = current.left
        return current

    def inOrderTraversal(self, node):
        """
        Performs an in-order traversal starting from the given node (left, root, right).
        """
        if node:
            self.inOrderTraversal(node.left)
            print(node.value)
            self.inOrderTraversal(node.right)

    def inOrderTraversalWrapper(self):
        """
        Wrapper function to start the in-order traversal from the root node.
        """
        self.inOrderTraversal(self.root)

    def inOrderTraversalIterative(self):
        """
        Performs an iterative in-order traversal using a stack instead of recursion.
        """
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.value)
            current = current.right

    def preOrderTraversal(self, node):
        """
        Performs a pre-order traversal starting from the given node (root, left, right).
        """
        if node:
            print(node.value)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def preOrderTraversalWrapper(self):
        """
        Wrapper function to start the pre-order traversal from the root node.
        """
        self.preOrderTraversal(self.root)

    def postOrderTraversal(self, node):
        """
        Performs a post-order traversal starting from the given node (left, right, root).
        """
        if node:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node.value)

    def postOrderTraversalWrapper(self):
        """
        Wrapper function to start the post-order traversal from the root node.
        """
        self.postOrderTraversal(self.root)

    def inOrderSuccessor(self, value):
        # Search for the node with the given value
        node = self.search(value)
        if node is None:
            # If node is not found, return None
            return None

        # Case 1: If the node has a right subtree
        if node.right:
            # Find the leftmost node in the right subtree
            current = node.right
            while current.left:
                current = current.left
            # The leftmost node in the right subtree is the successor
            return current.value

        # Case 2: If the node does not have a right subtree
        successor = None  # Potential successor
        ancestor = self.root
        """
        If the node does not have a right subtree, the inOrder successor will be the lowest ancestor of the node,
        whose left child is also an ancestor of the node.
        This is because, if the node does not have a right subtree, the successor will be the next higher node in terms
        of value, which will be an ancestor in its path towards the root.

                                  20
                                 /  \
                                10    30
                               /  \     \
                              5    15    40
                                     \
                                     17
        Example, finding the successor of node 17. The inorder successor is 20. It is the lowest ancestor whose left
         child is also an ancestor of our 17

        """
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

    def inOrderSuccessorParentNode(self, value):
        # Search for the node with the given value
        node = self.search(value)
        if node is None:
            # If node is not found, return None
            return None

        # Case 1: If the node has a right subtree
        if node.right:
            # Find the leftmost node in the right subtree
            current = node.right
            while current.left:
                current = current.left
            # The leftmost node in the right subtree is the successor
            return current.value

        # Case 2: If the node does not have a right subtree
        parent = node.parent
        """
        Using the same logic as above, we trace back from our node to the lowest ancestor whose left child is also an 
        ancestor of the original node.


                                  20
                                 /  \
                                10    30
                               /  \     \
                              5    15    40
                                     \
                                     17
        We start from 17 as parent. We trace upwards until parent is not None and until node is the right child of parent.

        Let x = 17, y = 15.
        y is not None and x == y.right. Enter while loop, update x and y. x = y = 15. y = y.parent = 10.
        y is not None and x == y.right. Enter while loop, update x and y. x = y = 10. y = y.parent = 20.
        y is not None but x != y.right. Exit while loop.
        20 is our inorder successor.
        """
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent

        # If a valid parent (successor) is found, return its value
        if parent is not None:
            return parent.value
        else:
            # If no valid parent (successor) is found, return None
            return None

    def inOrderPredecessor(self, value):
        # Search for the node with the given value
        node = self.search(value)
        if node is None:
            # If node is not found, return None
            return None

        # Case 1: If the node has a left subtree
        if node.left:
            # Find the rightmost node in the left subtree
            current = node.left
            while current.right:
                current = current.right
            # The rightmost node in the left subtree is the predecessor
            return current.value

        # Case 2: If the node does not have a left subtree
        ancestor = self.root
        predecessor = None
        # Traverse the tree from the root to the node
        # The predecessor will be the deepest node for which the given node is in the right subtree
        while ancestor != node:
            if value > ancestor.value:
                predecessor = ancestor
                ancestor = ancestor.right
            else:
                ancestor = ancestor.left

        # Return the predecessor's value if it exists
        if predecessor:
            return predecessor.value
        else:
            # If no predecessor is found, return None
            return None

    def inOrderPredecessorWithParentNode(self, value):
        # Search for the node with the given value
        node = self.search(value)
        if node is None:
            # If node is not found, return None
            return None

        # Case 1: If the node has a left subtree
        if node.left:
            # Find the rightmost node in the left subtree
            current = node.left
            while current.right:
                current = current.right
            # The rightmost node in the left subtree is the predecessor
            return current.value

        # Case 2: If the node does not have a left subtree
        x = node
        y = node.parent
        # Traverse up using parent pointers until we find a node
        # that is the right child of its parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        # If we found a parent that has x as its right child,
        # then this parent is the in-order predecessor
        if y:
            return y.value
        else:
            # If no such parent exists, return None
            return None

    def deleteNode(self, node, value):
        """
        Delete a node with the given value from the binary search tree.

        Args:
        node (Node): The root of the subtree in which to delete the node.
        value (int): The value of the node to be deleted.

        Returns:
        Node: The root of the modified subtree.
        """
        if node is None:
            return None

        # If the value to be deleted is smaller than the root's value,
        # then it lies in the left subtree
        if value < node.value:
            node.left = self.deleteNode(node.left, value)
        # If the value to be deleted is greater than the root's value,
        # then it lies in the right subtree
        elif value > node.value:
            node.right = self.deleteNode(node.right, value)
        else:
            # Node to delete is found
            # If the node to be deleted does not have any children (leaf node),
            # just delete the node and return None
            if node.right is None and node.left is None:
                return None
            # If the node has only left child, return the left child
            elif node.right is None:
                return node.left
            # If the node has only right child, return the right child
            elif node.left is None:
                return node.right
            # If the node has both left and right child
            # Find the minimum value in the right subtree, i.e. the inorder successor
            else:
                current = node.right
                while current.left:
                    current = current.left
                # Replace the value of the node to be deleted with the inorder successor's value
                node.value = current.value
                # Delete the inorder successor
                node.right = self.deleteNode(node.right, current.value)
        return node

    def deleteNodeWrapper(self, value):
        """
        This is a wrapper function that initiates the deletion of a node with the given value from the binary search tree.

        Args:
        value (int): The value of the node to be deleted.

        Returns:
        None
        """
        self.root = self.deleteNode(self.root, value)

