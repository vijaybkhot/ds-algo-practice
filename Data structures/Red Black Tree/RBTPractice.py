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
        z = Node(value=value, color="RED")
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
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # Uncle
                if y.color == "RED":
                    y.color = "BLACK"
                    z.parent.color = "BLACK"
                    z.parent.parent = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left  # Uncle
                if y.color == "RED":
                    y.color = "BLACK"
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.left_roatate(z.parent.parent)
        self.root.color = "BLACK"
        



