class MinHeap:

    def __init__(self):
        self.arr = [0] # 0 is dummy value for easier math
 

    def push(self, val: int) -> None:
        self.arr.append(val)
        self._bubble_up(index=len(self.arr)-1)


    def pop(self) -> int:
        if len(self.arr) == 1:
            return -1
        if len(self.arr) == 2:
            return self.arr.pop()
        
        res = self.arr[1]
        self.arr[1] = self.arr.pop()
        self._bubble_down(index=1)
        return res
        

    def top(self) -> int:
        return self.arr[1] if len(self.arr) > 1 else -1
        

    def heapify(self, nums: List[int]) -> None:
        self.arr = [0] + nums
        for i in reversed(range(1, len(nums)//2+1)):
            self._bubble_down(index=i)


    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]


    def _bubble_up(self, index: int) -> None:
        parent = index // 2
        while index > 1 and self.arr[parent] > self.arr[index]:
            self.swap(parent, index)
            index = parent
            parent = index // 2


    def _bubble_down(self, index: int) -> None:
        child = index * 2 # left child
        if child >= len(self.arr):
            return
        # if right child and right child is smaller than left add 1 to child
        if len(self.arr) > child+1 and self.arr[child+1] < self.arr[child]:
            child += 1 # we will swap right child
        if self.arr[child] >= self.arr[index]:
            return
        self.swap(index, child)
        self._bubble_down(child)








