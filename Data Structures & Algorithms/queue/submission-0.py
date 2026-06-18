class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node("dummy head")
        self.tail = Node("dummy tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        new_node, prev_node, next_node = Node(value), self.tail.prev, self.tail
        new_node.next = next_node
        new_node.prev = prev_node
        next_node.prev = new_node
        prev_node.next = new_node


    def appendleft(self, value: int) -> None:
        new_node, prev_node, next_node = Node(value), self.head, self.head.next
        new_node.next = next_node
        new_node.prev = prev_node
        next_node.prev = new_node
        prev_node.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        target_node = self.tail.prev
        prev_node = target_node.prev
        next_node = self.tail
        prev_node.next = next_node
        next_node.prev = prev_node
        return target_node.val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        target_node = self.head.next
        prev_node = self.head
        next_node = target_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        return target_node.val