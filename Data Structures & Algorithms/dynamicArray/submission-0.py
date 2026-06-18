class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.pointer = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.pointer:
            self.resize()
        self.arr[self.pointer] = n
        self.pointer += 1

    def popback(self) -> int:
        self.pointer -= 1
        res = self.arr[self.pointer]
        self.arr[self.pointer] = None
        return res

    def resize(self) -> None:
        new_arr = [None] * (self.capacity * 2)
        self.capacity = len(new_arr)
        for i, num in enumerate(self.arr):
            new_arr[i] = num
        self.arr = new_arr

    def getSize(self) -> int:
        return self.pointer

    def getCapacity(self) -> int:
        return self.capacity
