class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix)-1, len(matrix[0])-1

        top, bottom = 0, ROWS
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break

        # if not (top <= bottom):
        #     return False

        row = top + (bottom - top) // 2
        l, r = 0, COLS
        while l <= r:
            mid = l + (r-l) // 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False