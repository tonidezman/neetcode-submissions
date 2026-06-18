class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.arr = [ListNode(0) for _ in range(10_000)]
        # self.counter = 0

    def add(self, key: int) -> None:
        idx = self.hash_function(key)
        prev = None
        curr = self.arr[idx]
        while curr:
            if curr.next and curr.next.val == key:
                return
            prev = curr
            curr = curr.next
        prev.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        idx = self.hash_function(key)
        curr = self.arr[idx]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        idx = self.hash_function(key)
        curr = self.arr[idx]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False

    def hash_function(self, key: int) -> int:
        return key % len(self.arr)



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)