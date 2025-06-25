from enum import Enum

class Color(Enum):
    RED = 0
    BLACK = 1

    def switch(self):
        return Color.BLACK if self == Color.RED else Color.RED

class RBTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = RBNode(value, Color.RED)
        else:
            inserted = self.root.insert(value)
            self.root = self.fix_insert(inserted)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == Color.RED:
            parent = node.parent
            grandparent = parent.parent
            if parent == grandparent.left:
                uncle = grandparent.right
                if uncle and uncle.color == Color.RED:
                    parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    grandparent.color = Color.RED
                    node = grandparent
                else:
                    if node == parent.right:
                        node = parent
                        self.rotate_left(node)
                    parent.color = Color.BLACK
                    grandparent.color = Color.RED
                    self.rotate_right(grandparent)
            else:
                uncle = grandparent.left
                if uncle and uncle.color == Color.RED:
                    parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    grandparent.color = Color.RED
                    node = grandparent
                else:
                    if node == parent.left:
                        node = parent
                        self.rotate_right(node)
                    parent.color = Color.BLACK
                    grandparent.color = Color.RED
                    self.rotate_left(grandparent)
        self.root.color = Color.BLACK
        return self.root

    def delete(self, value):
        if self.root is not None:
            self.root, sibling = self.root.delete(value)
            self.root = self.fix_delete(sibling)

    def fix_delete(self, node):
        while node != self.root and (node is None or node.color == Color.BLACK):
            parent = node.parent if node else None
            if node == parent.left:
                sibling = parent.right
                if sibling and sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    parent.color = Color.RED
                    self.rotate_left(parent)
                    sibling = parent.right
                if (sibling.left is None or sibling.left.color == Color.BLACK) and \
                        (sibling.right is None or sibling.right.color == Color.BLACK):
                    sibling.color = Color.RED
                    node = parent
                else:
                    if sibling.right is None or sibling.right.color == Color.BLACK:
                        if sibling.left:
                            sibling.left.color = Color.BLACK
                        sibling.color = Color.RED
                        self.rotate_right(sibling)
                        sibling = parent.right
                    sibling.color = parent.color
                    parent.color = Color.BLACK
                    if sibling.right:
                        sibling.right.color = Color.BLACK
                    self.rotate_left(parent)
                    node = self.root
            else:
                sibling = parent.left
                if sibling and sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    parent.color = Color.RED
                    self.rotate_right(parent)
                    sibling = parent.left
                if (sibling.left is None or sibling.left.color == Color.BLACK) and \
                        (sibling.right is None or sibling.right.color == Color.BLACK):
                    sibling.color = Color.RED
                    node = parent
                else:
                    if sibling.left is None or sibling.left.color == Color.BLACK:
                        if sibling.right:
                            sibling.right.color = Color.BLACK
                        sibling.color = Color.RED
                        self.rotate_left(sibling)
                        sibling = parent.left
                    sibling.color = parent.color
                    parent.color = Color.BLACK
                    if sibling.left:
                        sibling.left.color = Color.BLACK
                    self.rotate_right(parent)
                    node = self.root
        if node:
            node.color = Color.BLACK
        return self.root

    def rotate_left(self, node):
        right = node.right
        node.right = right.left
        if right.left:
            right.left.parent = node
        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right
        return right

    def rotate_right(self, node):
        left = node.left
        node.left = left.right
        if left.right:
            left.right.parent = node
        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        left.right = node
        node.parent = left
        return left

    def search(self, value):
        if self.root is not None:
            return self.root.search(value)
        return False

class RBNode:
    def __init__(self, value, color, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.color = color
        self.parent = parent

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = RBNode(value, Color.RED, self)
                return self.left
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = RBNode(value, Color.RED, self)
                return self.right


    def delete(self, value, sibling=None):
        if value == self.value:
            if self.left is None and self.right is None:
                return None, sibling
            if self.left and self.right:
                succ = self.get_succ()
                self.value = succ.value
                self.right, sibling = self.right.delete(value, self.left)
                return self, sibling
            if self.left:
                self.value = self.left.value
                self.left = None
                return self, sibling
            elif self.right:
                self.value = self.right.value
                self.right = None
                return self, sibling
        elif value < self.value and self.left:
            self.left, sibling = self.left.delete(value, self.right)
            return self, sibling
        elif value > self.value and self.right:
            self.right, sibling = self.right.delete(value, self.left)
            return self, sibling

    def get_succ(self):
        current = self
        while current.left:
            current = current.left
        return current

    def search(self, value):
        if value == self.value:
            return True
        elif value < self.value and self.left:
            return self.left.search(value)
        elif value > self.value and self.right:
            return self.right.search(value)
        return False

class RBTreeImperative(RBNode):
    def __init__(self, value, color, parent):
        super().__init__(value, color)
        self.parent = parent

class RBTreeFunctional(RBNode):
    def __init__(self, value, color, left, right):
        super().__init__(value, color)
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

def is_rb_kept(tree):
    pass

def is_bst(tree):
    pass

def is_balanced(tree):
    pass