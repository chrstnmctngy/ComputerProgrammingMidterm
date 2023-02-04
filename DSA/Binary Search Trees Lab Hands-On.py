class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def Search(self, value):
        if self.key == value:
            print("Value Exist.")
            return

        if value < self.key:
            if self.left:
                self.left.Search(value)
            else:
                print("Value Does Not Exist.")
        else:
            if self.right:
                self.right.Search(value)
            else:
                print("Value Does Not Exist.")

    def Insert(self, value):
        if self.key is None:
            self.key = value
            return

        if self.key > value:
            if self.left:
                self.left.Insert(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.Insert(value)
            else:
                self.right = Node(value)


    def Delete(self, value):
        if self.key is None:
            print("Empty Node")
            return
        if self.key == value:
            print("The Value is Deleted.")
            return
        if value > self.key:
            if self.right:
                self.right = self.right.Delete(value)
            else:
                print("Value does not exist.")
        elif value < self.key:
            if self.left:
                self.left = self.left.Delete(value)
            else:
                print("Value does not exist.")
        else:
            if self.right is None:
                x = self.left
                self = None
                return x
            if self.left is None:
                x = self.right
                self = None
                return x

            vertex = self.right

            while vertex.left:
                vertex = Node.left
            self.key = vertex.key
            self.right = self.right.Delete(vertex.key)
        return self


BinarySearchTree = Node(30)
BinarySearchTree.Insert(22)
BinarySearchTree.Insert(5)
BinarySearchTree.Insert(82)
BinarySearchTree.Insert(55)
BinarySearchTree.Insert(39)
BinarySearchTree.Insert(81)

BinarySearchTree.Search(22)
BinarySearchTree.Search(55)
BinarySearchTree.Search(30)
BinarySearchTree.Search(1)

BinarySearchTree.Delete(81)
BinarySearchTree.Delete(55)