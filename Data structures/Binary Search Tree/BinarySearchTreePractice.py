class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTreePractice:
    def __init__(self):
        self.root = None

    def insert_iterative(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return self
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        return self
                    else:
                        current = current.left
                elif value < current.value:
                    if current.right is None:
                        current.right = new_node
                        return self
                    else:
                        current = current.right
                else:
                    print("The value already exists in the BST. Cannot insert duplicate values")
                    return self

    def insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        else:
            if value < node.value:
                node.left = self.insert_recursive(node.left, value)
            elif value > node.value:
                node.right = self.insert_recursive(node.right, value)
            else:
                print("value already exists in the BST. Cannot enter duplicate values")
        return node

    def insert_recursive_wrapper(self, value):
        self.root = self.insert_recursive(self.root, value)

    def insert_recursive_1(self, node, value):
        if node is None:
            return Node(value)
        else:
            if value < node.value:
                node.left = self.insert_recursive_1(node.left, value)
            elif value > node.value:
                node.right = self.insert_recursive_1(node.right, value)
            else:
                print("Value already exists in the BST. Cannot insert duplicate values.")
        return node

    def insert_recursive_wrapper_1(self, value):
        self.root = self.insert_recursive_1(self.root, value)
        return self.root

    def insert_recursive_2(self, node, value):
        if node is None:
            return Node(value)
        else:
            if value < node.value:
                node.left = self.insert_recursive_2(node.left, value)
            elif value > node.value:
                node.right = self.insert_recursive_2(node.right, value)
            else:
                print("Value already exists in the tree. Cannot insert duplicate values")

        return node

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
                    # Found
                    return current
            return None

    def search_1(self, value):
        # Empty Tree
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
                    # Found
                    return current
            # Not found
            return None

    def search_recursive(self, node, value):
        if node is None or node.val == value:
            return node
        else:
            if value < node.value:
                return self.search_recursive(node.left, value)
            elif value > node.value:
                return self.search_recursive(node.right, value)

    def search_recursive_wrapper(self, value):
        return self.search_recursive(self.root, value)

    def search_recursive_1(self, node, value):
        if node is None or node.value == value:
            return node
        else:
            if value < node.value:
                return self.search_recursive_1(node.left, value)
            elif value > node.value:
                return self.search_recursive_1(node.right, value)

    def search_recursive_wrapper_1(self, value):
        return self.search_recursive_1(self.root, value)


    def delete_node(self, node: Node, value: int):
        if node is None:
            return node

        if value < node.value:
            # Recursively delete from the left subtree
            node.left = self.delete_node(node.left, value)
        elif value > node.value:
            # Recursively delete from the right subtree
            node.right = self.delete_node(node.right, value)
        else:
            # Node to deleted found
            if node.right is None and node.left is None:
                # Node has no children (leaf node)
                return None
            elif node.right is None:
                # If no right child, return left child
                return node.left
            elif node.left is None:
                # If no left child, return right child
                return node.right

            # Node has both left and right children
            # Find the minimum value in the right subtree
            curr = node.right
            while curr.left:
                curr = curr.left
            # Replace the node's value with the minimum value
            node.value = curr.value
            # Delete the node with the minimum value in the right subtree
            node.right = self.delete_node(node.right, curr.value)

        return node

    def delete_node_wrapper(self, value):
        self.root = self.delete_node(self.root, value)
        return self.root

    def delete_node_1(self, node, value):
        if node is None:
            # Node to delete not found
            return node

        if value < node.value:
            node.left = self.delete_node_1(node.left, value)
        elif value > node.value:
            node.right = self.delete_node_1(node.right, value)
        else:
            # Node to delete found
            if node.left is None and node.right is None:
                # No children
                return None
            elif node.right is None:
                # no right child, return left child
                return node.left
            elif node.left is None:
                # no left child, return right child
                return node.right
            # node has both left and right subtree
            # Find the minimum in right subtree
            curr = node.right
            while curr.left:
                curr = curr.left
            node.value = curr.value
            node.right = self.delete_node_1(node.right, curr.value)

        return node

    def delete_node_wrapper_1(self, value):
        self.root = self.delete_node_1(self.root, value)
        return self.root

    def delete_node_2(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.delete_node_2(node.left, value)
        elif value > node.value:
            node.right = self.delete_node_2(node.right, value)
        else:
            # Node to be deleted found
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # node has both left and right subtree
            # Find the minimum in right subtree
            curr = node.right
            while curr.left:
                curr = curr.left
            node.value = curr.value
            node.right = self.delete_node_2(node.right, curr.value)

        return node

    def delete_node_wrapper_2(self, value):
        self.root = self.delete_node_2(self.root, value)
        return self.root

    def delete_node_3(self, node: Node, value: int):
        if node is None:
            return None
        if value < node.value:
            node.left = self.delete_node_3(node.left, value)
        elif value > node.value:
            node.right = self.delete_node_3(node.right, value)
        else:
            # Node to be deleted found
            # No children
            if node.left is None and node.right is None:
                return None
            # Only right child
            elif node.left is None:
                return node.right
            # Only left child
            elif node.right is None:
                return node.left
            # Node has both left and right children
            # Find minimum in right subtree
            curr = node.right
            while curr.left:
                curr = curr.left
            node.value = curr.value
            node.right = self.delete_node_3(node.right, curr.value)

        return node

    def delete_node_wrapper_3(self, value):
        self.root = self.delete_node_3(self.root, value)
        return self.root


# Test cases
bst = BinarySearchTreePractice()

# Test case 1: Inserting elements into an empty BST
values1 = [10, 5, 15, 3, 7, 12, 18]
for val in values1:
    bst.root = bst.insert_recursive_2(bst.root, val)

# Test case 2: Inserting duplicate value
bst.root = bst.insert_recursive_2(bst.root, 10)  # Duplicate value
print(bst.root.value)  # Should print 10, as the duplicate value insertion should return None

# Test case 3: Inserting elements into a BST with existing nodes
values2 = [8, 20, 4, 9, 17]
for val in values2:
    bst.root = bst.insert_recursive_2(bst.root, val)

# Print the root node after insertion
print(bst.root.value)  # Should print the value of the root node of the BST