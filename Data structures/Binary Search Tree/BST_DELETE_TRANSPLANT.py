class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_iterative(self, value):
        new_node = Node(value)
        if self.root is None:
            return new_node
        else:
            current = self.root
            while current:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        current.left.parent = current
                        return self.root
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = new_node
                        new_node.parent = current
                        return self.root
                    else:
                        current = current.right
                else:
                    print("The value already exists in the BST. Cannot insert duplicate values")
                    return self.root

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

    def search_recursive(self, node, value):
        if node is None or value is None:
            return None
        elif node.value == value:
            return node
        elif value < node.value:
            return self.search_recursive(node.left, value)
        else:
            return self.search_recursive(node.right, value)

    def search(self, value):
        return self.search_recursive(self.root, value)

    def tree_minimum(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def transplant(self, u, v):
        # If u is the root of the tree, set the root to be v
        if u.parent is None:
            self.root = v
        # If u is the left child of its parent, set the left child of u's parent to be v
        elif u == u.parent.left:
            u.parent.left = v
        # If u is the right child of its parent, set the right child of u's parent to be v
        else:
            u.parent.right = v

        # If v is not None, set v's parent to be u's parent
        if v is not None:
            v.parent = u.parent

    def tree_delete(self, z):
        if z is None:
            return  # Do nothing if z is None

        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def inorder_successor(self, node):
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current.value
        else:
            y = node.parent
            while y is not None and node == y.right:
                node = y
                y = y.parent
            return y.value

    def inorder_successor_1(self, node):
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current.value
        else:
            y = node.parent
            while y is not None and y.right == node:
                node = y
                y = y.parent
            if y is not None:
                return y.value
            else:
                return None

    def inorder_successor_2(self, node):
        if node is None:
            return None
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current.value
        else:
            parent = node.parent
            while parent is not None and node == parent.right:
                node = parent
                parent = node.parent
            if parent is not None:
                return parent.value
            else:
                return None

    def inorder_successor_3(self, node):
        if node is None:
            return None
        else:
            if node.right:
                current = node.right
                while current.left:
                    current = current.left
                return current.value
            else:
                parent = node.parent
                while parent is not None and node == parent.right:
                    node = parent
                    parent = parent.parent
                if parent is not None:
                    return parent.value
                else:
                    return None

    def inorder_successor_4(self, node):
        if node is None:
            return None
        else:
            if node.right:
                current = node.right
                while current.left:
                    current = current.left
                return current.value
            else:
                parent = node.parent
                while parent is not None and node == parent.right:
                    node = parent
                    parent = parent.parent
                if parent is not None:
                    return parent.value
                else:
                    return None

    def inorder_successor_5(self, node):
        if node is None:
            return None
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current.value
        x = node
        y = node.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        if y is not None:
            return y.value
        else:
            return None

    def inorder_successor_6(self, value):
        node = self.search(value)
        if node is None:
            return None
        else:
            if node.right:
                current = node.right
                while current.left:
                    current = current.left
                return current.value
            x = node
            y = node.parent
            while y is not None and x == y.right:
                x = y
                y = y.parent
            if y is not None:
                return y.value
            else:
                return None

    def inorder_successor_7(self, value):
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
                x = node
                y = node.parent
                while y is not None and x == y.right:
                    x = y
                    y = y.parent
                if y is not None:
                    return y.value
                else:
                    return None

    def inorder_successor_8(self, value):
        node = self.search(value)
        if node is None:
            return None
        if node.right is not None:
            current = node.right
            while current.left:
                current = current.left
            return current.value
        # If the node has no right child
        # Find the successor which is the lowest ancestor whose left child is also an ancestor of the node
        x = node
        y = node.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        if y is not None:
            return y.value
        else:
            return None



# Create a binary search tree
bst = BinarySearchTree()
bst.root = Node(5)
bst.root.left = Node(3)
bst.root.right = Node(7)
bst.root.left.parent = bst.root
bst.root.right.parent = bst.root
bst.root.left.left = Node(2)
bst.root.left.right = Node(4)
bst.root.left.left.parent = bst.root.left
bst.root.left.right.parent = bst.root.left
bst.root.right.left = Node(6)
bst.root.right.right = Node(8)
bst.root.right.left.parent = bst.root.right
bst.root.right.right.parent = bst.root.right

# Test inorder successor for nodes with right subtree
assert bst.inorder_successor_8(3) == 4  # Successor of 3 is 4
assert bst.inorder_successor_8(5) == 6  # Successor of 5 is 6
assert bst.inorder_successor_8(7) == 8  # Successor of 7 is 8

# Test inorder successor for nodes without right subtree
assert bst.inorder_successor_7(2) == 3  # Successor of 2 is 3
assert bst.inorder_successor_7(4) == 5  # Successor of 4 is 5
assert bst.inorder_successor_7(6) == 7  # Successor of 6 is 7
assert bst.inorder_successor_7(8) == None  # Successor of 8 is None (no successor)

# Test inorder successor for the rightmost node
assert bst.inorder_successor_7(8) == None  # Rightmost node has no successor

# Test inorder successor for None node
assert bst.inorder_successor_7(None) == None  # None node has no successor

# Test inorder successor for root node with no right subtree
bst.root.right = None
assert bst.inorder_successor_7(5) == None  # Root node has no right subtree, so its successor is None

print("All test cases passed.")
