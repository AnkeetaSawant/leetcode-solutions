class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        counter = 0
        curr = self.head
        while curr:
            if counter == index:
                return curr.val
            counter = counter + 1
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)

        if not self.head:
            self.head = newNode
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return 

        newNode = Node(val)
        
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        counter = 0
        curr = self.head
        while curr and counter < index - 1:
            curr = curr.next
            counter += 1 

        if not curr:
            return

        newNode.next = curr.next
        curr.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return 
            
        counter = 0
        curr = self.head
        while curr and counter < index - 1:
            prev = curr
            curr = curr.next
            counter += 1
        if not curr or not curr.next:
            return 
        curr.next = curr.next.next

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.get(1)
obj.printList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)