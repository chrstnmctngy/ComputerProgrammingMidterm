class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def in_Order(self):
        print(self.key, end=" ")
        if self.left:
            self.left.in_Order()
        if self.right:
            self.right.in_Order()

    def pre_Order(self):
        if self.left:
            self.left.in_Order()
        print(self.key, end=" ")
        if self.right:
            self.right.in_Order()

    def post_Order(self):
        if self.left:
            self.left.in_Order()
        if self.right:
            self.right.in_Order()
        print(self.key, end=" ")

    def Insert(self, element):
        if self.key is None:
            self.key = element
            return
        if self.key > element:
            if self.left:
                self.left.Insert(element)
            else:
                self.left = Node(element)
        else:
            if self.right:
                self.right.Insert(element)
            else:
                self.right = Node(element)

BinarySearchTree = Node(30)
BinarySearchTree.Insert(22)
BinarySearchTree.Insert(5)
BinarySearchTree.Insert(82)
BinarySearchTree.Insert(55)
BinarySearchTree.Insert(39)
BinarySearchTree.Insert(81)

BinarySearchTree.in_Order()
print()
BinarySearchTree.pre_Order()
print()
BinarySearchTree.post_Order()