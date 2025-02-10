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
            return self
        else:
            current = self.root
            while True:
                if value == current.value:
                    print("The value already exists inside the tree. No duplicates allowed.")
                    return self
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        return self
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = new_node
                        return self
                    else:
                        current = current.right

    def insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self.insert_recursive(node.right, value)
        else:
            print("Value already exists in the BST. Cannot accept duplicate values.")
        return node

    def insert_recursive_wrapper(self, value):
        self.root = self.insert_recursive(self.root, value)

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

    def inorder_walk(self, node):
        if node is not None:
            self.inorder_walk(node.left)
            print(node.value)
            self.inorder_walk(node.right)

    def inorder_walk_wrapper(self):
        self.inorder_walk(self.root)

    def inorder_successor(self, value):
        node = self.search(value)
        # If the value is not present in the tree
        if node is None:
            return None

        # If the node is found, and it has a right subtree
        # The successor is the smallest element in the right subtree
        # find the smallest value in right subtree
        if node.right is not None:
            current = node.right
            while current.left:
                current = current.left
            return current.value

        # If the node does not have a right subtree
        # We have to find an ancestor that is the next in the inorder than our original node
        # We start from the root of the tree and traverse towards our node
        successor = None  # Potential successor
        ancestor = self.root
        # If the node does not have a right subtree, then the successor will be
        # the lowest ancestor of the node whose left child is also an ancestor of the node.
        # This is because if a node does not have a right child, its inorder successor will be
        # the next higher node in terms of value, which will be an ancestor in the path towards the root.
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

    def inorder_predecessor(self, value):
        node = self.search(value)
        # If the value is not present in the tree
        if node is None:
            return None

        # If the node has a left subtree, find the maximum value in the left subtree
        if node.left is not None:
            current = node.left
            while current.right:
                current = current.right
            return current.value

        # If the node does not have a left subtree, find the ancestor
        # Start with the root node as predecessor
        predecessor = None
        ancestor = self.root
        while ancestor != node:
            if node.value > ancestor.value:
                predecessor = ancestor
                ancestor = ancestor.right
            else:
                ancestor = ancestor.left

        if predecessor:
            return predecessor.value
        else:
            return None

    def tree_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def tree_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.right


# def is_leaf(self, node):
#     return node.left == node.right is None
#
# def get_parent(self, node):
#     current = self.root
#     while current is not None:
#         if node.value == current.left.value:
#             parent = current
#             return parent
#         elif node.value == current.right.value:
#             parent = current
#             return parent
#         else:
#             if node.value < current.value:
#                 current = current.left
#             elif node.value > current.value:
#                 current = current.right
#             else:
#                 print("Parent not found. The current node is the root of the tree.")
#                 return None
#
# def one_child(self, node):
#     one_child = True
#     if (node.right == node.left is None) or (node.right is not None and node.left is not None):
#         one_child = False
#     return one_child
#
# def two_children(self, node):
#     return node.right is not None and node.left is not None
#
# def min_value_node(self, node):
#     current = node
#     while current.left is not None:
#         current = current.left
#     return current
#
# def in_order_successor(self, node):
#     if node.right is not None:
#         successor = self.min_value_node(node)
#     else:
#         successor = None
#         current = self.root
#         while current is not None:
#             if node.value < current.value:
#                 successor = current
#                 current = current.left

# def delete(self, value):
#     x = self.search(value)
#     if x is None:
#         # Not found
#         return None
#     ret = x
#     # Delete leaf node
#     if self.is_leaf(x):
#         parent = self.get_parent(x)
#         if parent.left.value == x.value:
#             parent.left = None
#         elif parent.right.value == x.value:
#             parent.right = None
#         return ret
#     if self.one_child(x):
#         parent = self.get_parent(x)
#         if parent.left.value == x.value:
#             if x.left is None:
#                 # x has only one child, which is the right child
#                 parent.left = x.right
#                 return ret
#             elif x.right is None:
#                 # x has only one child, which is the left child
#                 parent.left = x.left
#                 return ret
#         elif parent.right.value == x.value:
#             if x.left is None:
#                 # x has only one child, which is the right child
#                 parent.right = x.right
#                 return ret
#             elif x.right is None:
#                 # x has only one child, which is the left child
#                 parent.right = x.left
#                 return ret


# Create a binary search tree
bst = BinarySearchTree()

# Insert some values
bst.insert_iterative(50)
bst.insert_iterative(30)
bst.insert_iterative(20)
bst.insert_iterative(40)
bst.insert_iterative(70)
bst.insert_iterative(60)
bst.insert_iterative(80)

# Perform inorder traversal and print the values
bst.inorder_walk_wrapper()

# Test search function
print(bst.search(70).value)  # Should print 70

# Test delete function
bst.delete_node(bst.root, 30)
print(bst.search(30))  # Should print None, as 30 has been deleted

# Insert and delete edge cases
bst.insert_recursive(bst.root, value=10)
bst.delete_node(bst.root, 50)
print(bst.search(50))  # Should print None, as 50 has been deleted
print(bst.search(10).value)  # Should print 10

# Test insertion of duplicate value
bst.insert_iterative(20)  # Should print "The value already exists inside the tree. No duplicates allowed."
