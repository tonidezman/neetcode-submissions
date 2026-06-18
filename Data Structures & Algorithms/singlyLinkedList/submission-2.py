class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        curr = self.head
        while index > 0 and curr:
            curr = curr.next
            index -= 1
        if curr is None:
            return -1
        return curr.val
        
    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        newHead.next = self.head
        self.head = newHead
        self.size += 1

    def insertTail(self, val: int) -> None:
        prev = None
        curr = self.head
        while curr:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = Node(val)
            self.size += 1
            return
        self.size += 1
        prev.next = Node(val)

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        if index == 0 and self.head:
            self.head = self.head.next
            return True
        prev = None
        curr = self.head
        while index > 0 and curr:
            prev = curr
            curr = curr.next
            index -= 1

        self.size -= 1
        if prev is None:
            return False
        if prev.next:
            prev.next = prev.next.next
            return True
        prev.next = None
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
