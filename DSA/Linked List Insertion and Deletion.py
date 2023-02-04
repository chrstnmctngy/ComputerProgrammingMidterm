print("Submitted by: Christian R. Macatangay (1R12)")

print()

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def PrintList(self):
        ListVal = self.head
        while ListVal:
            print (ListVal.data)
            ListVal = ListVal.next
            
    def Insertion(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

    def Deletion(self, position):
        if self.head is None:
            return
        
        Delete = self.head
        if position == 0:
            self.head = Delete.next
            Delete = None
            return
        
        for i in range(position - 1):
            Delete = Delete.next
            if Delete is None:
                break

        Remove = Delete.next.next
        Delete.next = None
        Delete.next = Remove

list = LinkedList()
print("Insertion Linked List:")
list.Insertion("A")
list.Insertion("B")
list.Insertion("C")
list.Insertion("D")
list.Insertion("E")
list.PrintList()

print()

print("Deletion Linked List:")
list.Deletion(0)
list.PrintList()