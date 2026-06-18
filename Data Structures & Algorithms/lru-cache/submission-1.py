class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.hsh = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if not key in self.hsh:
            return -1
        node = self.hsh[key]
        self.remove(node)
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hsh:
            node = self.hsh[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return

        node = Node(key, value)
        self.hsh[key] = node
        self.insert(node)
        if len(self.hsh) > self.cap:
            node_to_del = self.head.next
            del self.hsh[node_to_del.key]
            self.remove(node_to_del)
        

    def insert(self, node: Node) -> None:
        prev, nxt = self.tail.prev, self.tail
        node.next, node.prev = nxt, prev
        prev.next = self.tail.prev = node


    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = node.next, node.prev









