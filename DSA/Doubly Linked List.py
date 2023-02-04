print("Submitted by: Christian R. Macatangay (1R12)")

print()

class Node:    
    def __init__(self, data = None):    
        self.data = data   
        self.previous = None    
        self.next = None   
            
class DoublyLinkedList:    
    def __init__(self):    
        self.head = None    
        self.tail = None   
            
    def PrintList(self, data):      
        NewNode = Node(data)    
            
        if(self.head == None):      
            self.head = self.tail = NewNode    
            self.head.previous = None      
            self.tail.next = None    
        else:    
            self.tail.next = NewNode     
            NewNode.previous = self.tail      
            self.tail = NewNode   
            self.tail.next = None  
    
    def Output(self):     
        Result = self.head   
        if(self.head == None):    
            print("List is empty")    
            return;    
        print("Doubly Linked List: ")    
        while(Result != None):      
            print(Result.data)   
            Result = Result.next  
                          
DoublyList = DoublyLinkedList()   
DoublyList.PrintList("A")   
DoublyList.PrintList("B")   
DoublyList.PrintList("C")    
DoublyList.PrintList("D")    
DoublyList.PrintList("E")    
      
DoublyList.Output() 