class ListNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.arr = [ListNode(0, 0) for _ in range(10**4)]
        

    def put(self, key: int, value: int) -> None:
        idx = key % len(self.arr)
        prev = None
        curr = self.arr[idx]
        while curr:
            if curr.next and curr.next.key == key:
                curr.next.val = value
                return
            prev = curr
            curr = curr.next
        prev.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        idx = key % len(self.arr)
        prev = None
        curr = self.arr[idx]
        while curr:
            if curr.next and curr.next.key == key:
                return curr.next.val
            prev = curr
            curr = curr.next
        return -1
        

    def remove(self, key: int) -> None:
        idx = key % len(self.arr)
        curr = self.arr[idx]
        while curr:
            if curr.next and curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
