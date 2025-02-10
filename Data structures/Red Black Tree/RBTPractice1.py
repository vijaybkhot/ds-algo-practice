class Node:
    def __init__(self, value, color="RED"):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = color
        self.duplicate_counter = 1


class RedBlackTree:
    def __init__(self):
        self.nil = Node(value=None, color="BLACK")
        self.root = self.nil

    def insert(self, value):
        # First using the normal two pointer method to insert a node in the BST
        z = Node(value)  # Node to be inserted
        y = self.nil  # Parent node initialization
        x = self.root  # Traversal node initialization
        while x != self.nil:
            y = x
            if z.value < x.value:
                x = x.left
            elif z.value > x.value:
                x = x.right
            else:
                x.duplicate_counter += 1
                print("Value already exists in the BST. Incremented the duplicate counter for the value node.")
                return
        z.parent = y
        if y == self.nil:  # Update root if tree is empty
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
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":  # If the parent is red and uncle is red
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:  # If the parent is red and uncle is black
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)
            else:  # z.parent is the right child of its parent
                y = z.parent.parent.left  # y is the uncle node and is the left child of z's parents parent
                if y.color == "RED":  # Uncle is Red and parent is Red
                    y.color = "BLACK"
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:  # Uncle is black and parent is red
                    if z == z.parent.left:  # z is a left child of its parent. Case 2: z, z.p and z.p.p form a triangle
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "BLACK"  # Case 3 z, z.p, z.p.p are linked in a straight line
                    z.parent.parent.color = "RED"
                    self.left_rotate(z.parent.parent)
        self.root.color = "BLACK"

    def left_rotate(self, x):
        # Set y as the right child of x
        y = x.right
        # Link y's left child to right side of x
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        # Replace x with y. Link y with x's parent
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        # Make x left child of y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        # Set x's left child as y
        y = x.left
        # Shift y's right child on to x as x's left child
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        # Replace x with y.
        # Link y to x's parent
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        # Make x y's right child
        y.right = x
        x.parent = y


def test_black_height_and_inorder_walk():
    # Initialize a Red-Black Tree
    rbt = RedBlackTree()

    # Insert values into the Red-Black Tree
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(30)
    rbt.insert(15)
    rbt.insert(25)
    rbt.insert(35)

    # Perform inorder walk
    def inorder_walk(node):
        if node != rbt.nil:
            inorder_walk(node.left)
            print(node.value, node.color)
            inorder_walk(node.right)

    print("Inorder Walk:")
    inorder_walk(rbt.root)

    # Test black height of the tree
    def black_height(node):
        if node == rbt.nil:
            return 0
        left_black_height = black_height(node.left)
        right_black_height = black_height(node.right)
        if left_black_height != right_black_height:
            raise ValueError("Black height of left and right subtrees does not match")
        return left_black_height + (1 if node.color == "BLACK" else 0)

    black_height_root = black_height(rbt.root)
    print("Black Height of Tree:", black_height_root)

    # Check if black height is consistent throughout the tree
    def check_black_height_consistency(node):
        if node == rbt.nil:
            return True
        left_consistency = check_black_height_consistency(node.left)
        right_consistency = check_black_height_consistency(node.right)
        return left_consistency and right_consistency and (black_height(node.left) == black_height(node.right))

    if check_black_height_consistency(rbt.root):
        print("Black Height is consistent throughout the tree")
    else:
        print("Black Height is not consistent throughout the tree")
        # Test case 1: Balanced tree with black height 2
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(5)
    rbt.insert(15)
    assert black_height(rbt.root) == 2

    # Test case 2: Unbalanced tree with black height 3
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(5)
    rbt.insert(15)
    rbt.insert(20)
    assert black_height(rbt.root) == 3

    # Test case 3: Tree with duplicate values
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(5)
    rbt.insert(15)
    rbt.insert(5)  # Duplicate value
    assert black_height(rbt.root) == 2

    # Test case 4: Tree with multiple levels
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(5)
    rbt.insert(15)
    rbt.insert(3)
    rbt.insert(7)
    rbt.insert(12)
    rbt.insert(18)
    rbt.insert(1)
    assert black_height(rbt.root) == 3

    print("All test cases passed")


# Run the test function
test_black_height_and_inorder_walk()
