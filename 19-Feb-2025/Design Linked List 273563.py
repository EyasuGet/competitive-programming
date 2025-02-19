# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        start = 0
        while curr and start < index:
            curr = curr.next
            start += 1
        return curr.data if curr else -1 

        
    def addAtHead(self, val: int) -> None:
        dummy = Node(val)
        dummy.next = self.head
        self.head = dummy
        self.size += 1

    
    def addAtTail(self, val: int) -> None:
        dummy = Node(val)
        if not self.head:
            self.head = dummy
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = dummy

        self.size += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        start = 0
        while curr and start < index - 1:
            curr = curr.next
            start += 1
        if curr:
            dummy = Node(val)
            dummy.next = curr.next
            curr.next = dummy


    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head:
            self.head = self.head.next
            return
        curr = self.head
        start = 0
        while curr and start < index - 1:
            curr = curr.next
            start += 1
        if curr and curr.next:
            curr.next = curr.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)