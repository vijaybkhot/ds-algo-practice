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
        z = Node(value=value)
        if self.root == self.nil:
            self.root = z
            z.parent = self.nil
            z.left = self.nil
            z.right = self.nil
            z.color = "BLACK"
            return
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if value < x.value:
                x = x.left
            elif value > x.value:
                x = x.right
            else:
                print("Value already exists in the RBT. Cannot add duplicate values.")
                return
        z.parent = y
        if z.value < y.value:
            y.left = z
        else:
            y.right = z
        z.left = z.right = self.nil
        z.color = "RED"
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z):
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:  # z.parent is a left child of its parent
                y = z.parent.parent.right  # Uncle node
                if y.color == "RED":  # Uncle Red
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:  # Uncle Black
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)
            else:  # z.parent is a right child of its parent
                y = z.parent.parent.left
                if y.color == "RED":  # Uncle Red
                    y.color = z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent
                else:  # Uncle Black
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.parent.color = "RED"
                    z.parent.color = "BLACK"
                    self.left_rotate(z.parent.parent)
        self.root.color = "BLACK"

    def left_rotate(self, x):
        # Assign x's right as y
        y = x.right
        # Make y's left as x's new right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        # Replace x with y
        # Link y with x's parent
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        # Make x y's left child
        x.parent = y
        y.left = x

    def right_rotate(self, x):
        # Assign y to x's left child
        y = x.left
        # Move y's right on to x's left side
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        # Replace x with y
        # Link x's parent with y
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y

        # Make x y's new left child
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