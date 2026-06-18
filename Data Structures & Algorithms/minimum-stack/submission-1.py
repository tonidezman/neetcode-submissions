class MinStack:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        

    def push(self, val: int) -> None:
        if len(self.stack_1) == 0:
            self.stack_1.append(val)
            self.stack_2.append(val)
            return
        self.stack_1.append(min(self.stack_1[-1], val))
        self.stack_2.append(val)
        

    def pop(self) -> None:
        self.stack_1.pop()
        self.stack_2.pop()
        

    def top(self) -> int:
        return self.stack_2[-1]
        

    def getMin(self) -> int:
        return self.stack_1[-1]
        

"""

i j
stacks
"""