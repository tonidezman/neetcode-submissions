class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.arr = [[0] * (COLS+1) for _ in range(ROWS+1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.arr[r][c+1]
                self.arr[r+1][c+1] = prefix + above

                # matrix_col = matrix[r-1][c-1]
                # up_col = self.arr[r-1][c]
                # left_col = self.arr[r][c-1]
                # self.arr[r][c] = matrix_col + up_col + left_col

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2 = row1+1, row2+1, col1+1, col2+1
        bottom_right = self.arr[row2][col2]
        above = self.arr[row1-1][col2]
        left = self.arr[row2][col1-1]
        top_left = self.arr[row1-1][col1-1]
        return bottom_right - above - left + top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)