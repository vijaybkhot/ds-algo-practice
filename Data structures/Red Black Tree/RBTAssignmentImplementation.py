from typing import Optional, List, Tuple
from enum import Enum


class Color(Enum):
    RED = 1
    BLACK = 2


class Node:
    def __init__(self, key: int, color: Color = Color.RED):
        self.key = key
        self.color = color
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.p: Optional[Node] = None


class RBTree:
    def __init__(self):
        self.T_nil = Node(0, Color.BLACK)
        self.T_nil.p = self.T_nil
        self.T_nil.left = self.T_nil
        self.T_nil.right = self.T_nil
        self.T_root = self.T_nil
        self.t_info = None

    def insert(self, key: int):
        z = Node(key, Color.BLACK)
        self.insert_node(z)

    def insert_node(self, z: Node):
        y = self.T_nil
        x = self.T_root
        while x != self.T_nil:
            y = x
            if z.key == x.key:
                raise ValueError("Value already exists in the RBTree. Cannot add duplicate values.")
            elif z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y == self.T_nil:
            self.T_root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

        z.left = self.T_nil
        z.right = self.T_nil
        z.color = Color.RED
        self.insert_fixup(z)

    def insert_fixup(self, z: Node):
        while z.p.color == Color.RED:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == Color.RED:
                    z.p.color = Color.BLACK
                    y.color = Color.BLACK
                    z.p.p.color = Color.RED
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = Color.BLACK
                    z.p.p.color = Color.RED
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == Color.RED:
                    z.p.color = Color.BLACK
                    y.color = Color.BLACK
                    z.p.p.color = Color.RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = Color.BLACK
                    z.p.p.color = Color.RED
                    self.left_rotate(z.p.p)
        self.T_root.color = Color.BLACK

    def left_rotate(self, x: Node):
        y = x.right
        x.right = y.left
        if y.left != self.T_nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.T_nil:
            self.T_root = y
        else:
            if x == x.p.left:
                x.p.left = y
            else:
                x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x: Node):
        y = x.left
        x.left = y.right
        if y.right != self.T_nil:
            y.right.p = x
        y.p = x.p
        if x.p == self.T_nil:
            self.T_root = y
        else:
            if x == x.p.right:
                x.p.right = y
            else:
                x.p.left = y
        y.right = x
        x.p = y

    def convert(self) -> List[int]:
        result = []
        self.convert_helper(self.T_root, result)
        return result

    def convert_helper(self, x: Node, result: List[int]):
        if x == self.T_nil:
            return
        self.convert_helper(x.left, result)
        result.append(x.key)
        self.convert_helper(x.right, result)

    def check_black_height(self) -> Tuple[bool, int]:
        return self.check_black_height_helper(self.T_root)

    def check_black_height_helper(self, x: Node) -> Tuple[bool, int]:
        if x == self.T_nil:
            return True, 1
        left_is_balanced, left_height = self.check_black_height_helper(x.left)
        right_is_balanced, right_height = self.check_black_height_helper(x.right)
        is_balanced = left_is_balanced and right_is_balanced and left_height == right_height
        return is_balanced, left_height + (1 if x.color == Color.BLACK else 0)

    def remove_all(self):
        self.remove_all_helper(self.T_root)
        self.T_root = self.T_nil

    def remove_all_helper(self, x: Node):
        if x == self.T_nil:
            return
        self.remove_all_helper(x.left)
        self.remove_all_helper(x.right)
        del x


if __name__ == "__main__":
    rb_tree = RBTree()
    rb_tree.insert(10)
    rb_tree.insert(5)
    rb_tree.insert(15)
    rb_tree.insert(3)
    rb_tree.insert(7)
    rb_tree.insert(13)
    rb_tree.insert(17)

    # Convert the RBTree to a sorted array
    sorted_array = rb_tree.convert()
    print("Sorted array:", sorted_array)

    # Check the black height of the RBTree
    is_balanced, black_height = rb_tree.check_black_height()
    print("Is balanced:", is_balanced)
    print("Black height:", black_height)

    # Remove all nodes from the RBTree
    rb_tree.remove_all()
