class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None


class HashTable:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.arr = [None] * self.cap
        self.size = 0


    def hashFunc(self, key: int) -> int:
        return key % self.cap


    def insert(self, key: int, value: int) -> None:
        index = self.hashFunc(key)
        if self.arr[index] is None:
            self.arr[index] = Node(key, value)
        else:
            prev = None
            curr = self.arr[index]
            while curr:
                if curr.key == key:
                    curr.val = value
                    return
                prev = curr
                curr = curr.next
            prev.next = Node(key, value)
        self.size += 1
        if self.getSize() / self.getCapacity() >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        index = self.hashFunc(key)
        curr = self.arr[index]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1


    def remove(self, key: int) -> bool:
        index = self.hashFunc(key)
        prev = None
        curr = self.arr[index]
        while curr:
            if curr.key == key:
                if prev is None:
                    self.arr[index] = curr.next
                else:
                    prev.next = curr.next
                self.size -= 1
                return True
            prev = curr
            curr = curr.next
        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.cap


    def resize(self) -> None:
        oldArr = self.arr
        self.cap *= 2
        self.size = 0
        self.arr = [None] * self.cap
        for curr in oldArr:
            while curr:
                self.insert(curr.key, curr.val)
                curr = curr.next
        


