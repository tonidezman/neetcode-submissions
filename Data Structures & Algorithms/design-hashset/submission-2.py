class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.arr = [None] * 10_000
        

    def add(self, key: int) -> None:
        k = key % len(self.arr)
        if self.arr[k] is None:
            self.arr[k] = ListNode(key)
        else:
            prev = None
            curr = self.arr[k]
            while curr:
                if curr.val == key:
                    return
                prev = curr
                curr = curr.next
            prev.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        k = key % len(self.arr)
        if self.arr[k] is None:
            return
        curr = self.arr[k]
        if curr.val == key:
            self.arr[k] = curr.next
            return
        prev = curr
        curr = curr.next
        while curr:
            if curr.val == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next


    def contains(self, key: int) -> bool:
        k = key % len(self.arr)
        if self.arr[k] is None:
            return False
        curr = self.arr[k]
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)