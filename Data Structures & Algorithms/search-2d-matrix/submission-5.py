class Solution:
    def bs(self, arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return True
            elif target > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix)-1, len(matrix[0])-1
        top, bottom = 0, ROWS
        while top <= bottom:
            mid = top + (bottom - top)//2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                return self.bs(matrix[mid], target)
        return False