class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.arr = [None] * capacity
        self.pointer = 0


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.pointer == self.cap:
            self.resize()
        self.arr[self.pointer] = n
        self.pointer += 1


    def popback(self) -> int:
        self.pointer -= 1
        res = self.arr[self.pointer]
        self.arr[self.pointer] = None
        return res
 

    def resize(self) -> None:
        self.cap *= 2
        newArr = [None] * self.cap
        for i in range(len(self.arr)):
            newArr[i] = self.arr[i]
        self.arr = newArr


    def getSize(self) -> int:
        return self.pointer
        
    
    def getCapacity(self) -> int:
        return self.cap
