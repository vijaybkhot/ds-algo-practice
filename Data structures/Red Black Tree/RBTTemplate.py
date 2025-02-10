class Node:
    def __init__(self, value, color="RED"):
        self.value = value  # Node's value
        self.color = color  # Node's color (RED or BLACK)
        self.left = None  # Left child
        self.right = None  # Right child
        self.parent = None  # Parent node


class RBT:
    def __init__(self):
        self.nil = Node(value=None, color="BLACK")  # Sentinel NIL node, used to represent leaves
        self.root = self.nil  # Initially, the root is the NIL node

    def insert(self, value):
        z = Node(value=value, color="RED")  # New node to be inserted, initially colored RED
        z.left = self.nil  # New node's left child is the NIL node
        z.right = self.nil  # New node's right child is the NIL node
        y = self.nil  # y will be the parent of x  # Change 1
        x = self.root  # Start from the root
        while x != self.nil:  # Traverse the tree to find the insertion point
            y = x
            if z.value < x.value:  # Go to the left subtree
                x = x.left
            else:  # Go to the right subtree
                x = x.right
        z.parent = y  # Set the parent of z to y
        if y == self.nil:  # If the tree is empty  # Change 2
            self.root = z  # New node becomes the root
        elif z.value < y.value:  # Insert z as the left or right child of y
            y.left = z
        else:
            y.right = z
        z.color = "RED"  # New node is colored RED  # Change 3
        self.insertFixup(z)  # Fix the tree to maintain Red-Black properties

    def insertFixup(self, z):
        while z.parent.color == "RED":  # Fixing violations of Red-Black properties
            if z.parent == z.parent.parent.left:  # If z's parent is the left child
                uncle = z.parent.parent.right  # z's uncle
                if uncle.color == "RED":  # Case 1: Uncle is RED
                    z.parent.color = "BLACK"  # Recolor parent and uncle
                    uncle.color = "BLACK"
                    z.parent.parent.color = "RED"  # Recolor grandparent
                    z = z.parent.parent  # Move z up to grandparent
                else:  # Uncle is BLACK
                    if z == z.parent.right:  # Case 2: z is the right child
                        z = z.parent
                        self.leftRotate(z)  # Left rotate around z's parent
                    z.parent.color = "BLACK"  # Case 3: z is the left child
                    z.parent.parent.color = "RED"
                    self.rightRotate(z.parent.parent)
            else:  # If z's parent is the right child
                uncle = z.parent.parent.left  # z's uncle
                if uncle.color == "RED":  # Case 1: Uncle is RED
                    z.parent.color = "BLACK"  # Recolor parent and uncle
                    uncle.color = "BLACK"
                    z.parent.parent.color = "RED"  # Recolor grandparent
                    z = z.parent.parent  # Move z up to grandparent
                else:  # Uncle is BLACK
                    if z == z.parent.left:  # Case 2: z is the left child
                        z = z.parent
                        self.rightRotate(z)  # Right rotate around z's parent
                    z.parent.color = "BLACK"  # Case 3: z is the right child
                    z.parent.parent.color = "RED"
                    self.leftRotate(z.parent.parent)
        self.root.color = "BLACK"  # Ensure the root is always BLACK

    def leftRotate(self, x):
        y = x.right  # y is x's right child
        x.right = y.left  # Move y's left subtree to x's right subtree
        if y.left != self.nil:
            y.left.parent = x  # Update parent pointer of y's left child
        y.parent = x.parent  # Link y's parent to x's parent
        if x.parent == self.nil:  # Change 4
            self.root = y  # If x was the root, y becomes the new root
        else:
            if x == x.parent.left:
                x.parent.left = y  # x was the left child
            else:
                x.parent.right = y  # x was the right child
        y.left = x  # Put x on y's left
        x.parent = y  # Update parent pointer of x

    def rightRotate(self, x):
        y = x.left  # y is x's left child
        x.left = y.right  # Move y's right subtree to x's left subtree
        if y.right != self.nil:
            y.right.parent = x  # Update parent pointer of y's right child
        y.parent = x.parent  # Link y's parent to x's parent
        if x.parent == self.nil:  # Change 5
            self.root = y  # If x was the root, y becomes the new root
        else:
            if x == x.parent.left:
                x.parent.left = y  # x was the left child
            else:
                x.parent.right = y  # x was the right child
        y.right = x  # Put x on y's right
        x.parent = y  # Update parent pointer of x

    def inOrderWalk(self, node):
        if node is not None and node != self.nil:
            self.inOrderWalk(node.left)  # Visit left subtree
            if node == self.root:
                print("This is the root node:")
            print(f"Value: {node.value}, color: {node.color}")
            self.inOrderWalk(node.right)  # Visit right subtree

    def blackHeight(self, node):
        if node is None or node == self.nil:  # Base case: NIL nodes
            return 0
        leftHeight = self.blackHeight(node.left)  # Black height of left subtree
        rightHeight = self.blackHeight(node.right)  # Black height of right subtree
        if leftHeight != rightHeight:
            raise ValueError("The red black tree is not balanced")  # Tree is not balanced
        return leftHeight + (1 if node.color == "BLACK" else 0)  # Count black nodes


# Example usage:
rbt = RBT()
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(15)
rbt.insert(25)
rbt.insert(5)


# Printing inorder to verify the tree structure
def inorder(tree, node):
    if node != tree.nil:
        inorder(tree, node.left)
        print(f"{node.value} ({node.color})", end=" ")
        inorder(tree, node.right)


inorder(rbt, rbt.root)
