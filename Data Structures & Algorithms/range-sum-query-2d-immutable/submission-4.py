class NumMatrix:
    matrix: List[List[int]]
    rows: int
    cols: int
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if row >= row1 and row <= row2 and col >= col1 and col <= col2:
                    sum += self.matrix[row][col]
        return sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# sum region -> figure out


# We could check inclusion in each array and add to a 
# 