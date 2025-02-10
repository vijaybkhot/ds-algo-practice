class Node:
    def __init__(self, value, color="RED"):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = color


class RBT:
    def __init__(self):
        self.nil = Node(value=None, color="BLACK")  # Sentinel Node
        self.root = self.nil

    # First using the normal two pointer insertion method for a BST
    def insert(self, value):
        z = Node(value)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z

        z.left = self.nil
        z.right = self.nil
        z.color = "RED"
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z):
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:  # z.parent is left child of its parent
                y = z.parent.parent.right  # Uncle
                if y.color == 'RED':  # If parent is red and uncle is red
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:  # If parent is red and uncle is black
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:  # z.parent is right child of its parent
                y = z.parent.parent.left  # Uncle
                if y.color == 'RED':  # If parent is red and uncle is red
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:  # If parent is red and uncle is black
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'BLACK'

    def left_rotate(self, x):
        # Set y as right child of x
        y = x.right
        # Link y's left child to x on the right side
        x.right = y.left
        if y.left == self.nil:
            y.left.parent = x
        # Link y to x's parent
        y.parent = x.parent
        if x.parent == self.nil:
            # If x is the root and its parent is Tree.nil, make y the root of the tree and its parent self.nil
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        # Make x, left child of y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        # Set y as left child of x
        y = x.left
        # Link right child of y to left of x
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        # Link y to x's parent
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        # Make x as right child of y
        y.left = x
        x.parent = y

    def inorder_walk(self, node):
        if node is not None:
            self.inorder_walk(node.left)
            print(node.value)
            self.inorder_walk(node.right)

