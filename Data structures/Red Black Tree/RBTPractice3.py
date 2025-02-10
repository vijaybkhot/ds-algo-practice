class Node:
    def __init__(self, value, color="RED"):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.nil = Node(value=None, color="BLACK")
        self.root = self.nil

    def insert(self, value):

        z = Node(value)
        if self.root == self.nil:
            self.root = z
            z.parent = self.nil
            z.left = self.nil
            z.right = self.nil
            z.color = "BLACK"
            return
        x = self.root
        y = self.nil
        while x != self.nil:
            y = x
            if z.value < x.value:
                x = x.left
            elif z.value > x.value:
                x = x.right
            else:
                print("Value already exists in the RBT. Cannot add duplicate values.")
                return
        if z.value < y.value:
            y.left = z
        else:
            y.right = z
        z.parent = y
        z.left = z.right = self.nil
        z.color = "RED"
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.parent.color == "RED":
            if z.parent.parent.left == z.parent:
                y = z.parent.parent.right   # Uncle
                if y.color == "RED":    # Uncle is red and parent is red
                    y.color = "BLACK"
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:   # Uncle is black
                    if z.parent.right == z:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.parent.color = "RED"
                    z.parent.color = "BLACK"
                    self.right_rotate(z.parent.parent)
            else:   # z.parent is the right child of its parent
                y = z.parent.parent.left    # Uncle
                if y.color == "RED":
                    y.color = "BLACK"
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:  # Uncle is black
                    if z.parent.left == z:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.left_rotate(z.parent.parent)
        self.root.color = "BLACK"

    def left_rotate(self, x):
        # assign y as right child of x
        y = x.right
        # Move y.left to x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        # Link y to x's parent
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y

        # Make x as the left child of y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        # Assign y as x's left child
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        y.right = x
        x.parent = y

    def inorder_walk(self, node):
        if node is not None and node != self.nil:
            self.inorder_walk(node.left)
            if self.root == node:
                print("Root is the following node:")
            print(f"Value: {node.value}, Color: {node.color}")
            self.inorder_walk(node.right)

    def black_height(self, node):
        if node is None or node == self.nil:
            return 0
        left_height = self.black_height(node.left)
        right_height = self.black_height(node.right)
        if left_height != right_height:
            raise ValueError("Tree is not balanced.")
        return left_height + (1 if node.color == "BLACK" else 0)


# Create a Red-Black Tree
rbt = RedBlackTree()

# Insert values into the tree
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(15)
rbt.insert(25)

# Calculate the black height of the tree
black_height = rbt.black_height(rbt.root)
print(f"Black height of the tree: {black_height}")

rbt.inorder_walk(rbt.root)





