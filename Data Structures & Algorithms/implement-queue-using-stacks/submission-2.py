class MyQueue:

    def __init__(self):
        self.l1 = []
        self.l2 = []

    def push(self, x: int) -> None:
        self.l1.append(x)
        

    def pop(self) -> int:
        self.dostuff()
        return self.l2.pop()
        

    def peek(self) -> int:
        self.dostuff()
        return self.l2[-1]
        
    def dostuff(self) -> None:
        if len(self.l2) > 0:
            return
        while self.l1:
            self.l2.append(self.l1.pop())

    def empty(self) -> bool:
        return len(self.l1 + self.l2) == 0
        
"""
l1 = [3]
l2 = [2, 1]
"""


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()