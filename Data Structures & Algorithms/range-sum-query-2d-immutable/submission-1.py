class NumMatrix:
    # Trick to make coding this easier
    # We actually precompute the sum matrix of size (row+1 x col+1)
    # Prefill top most row and left most column with 0s so we don't
    # have to worry about handling out of bound edge cases
    # Eg:
    # [0,0,0]
    # [0,4,5]
    # [0,1,7]

    def __init__(self, matrix: List[List[int]]):

        #initialize 2sd sum_matrix with 0s with a size offset
        ROWS, COLS = len(matrix), len(matrix[0])

        self.sum_matrix = [[0]*(COLS+1) for _ in range(ROWS+1)] 

        #O(ROWS x COLS)
        #Row and col iteration doesn't have an offset 
        #because we are going through the original matrix
        #The prefix is stored in the sum_matrix with +1 offset
        for row in range(0, ROWS):
            prefix = 0
            for col in range(0, COLS):
                prefix += matrix[row][col]
                above = self.sum_matrix[row][col+1]
                self.sum_matrix[row+1][col+1] = prefix+above

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Offset coords by 1 because prefix in sum_matrix is stored with a
        # +1 offset
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 +1, col2 + 1

        top = self.sum_matrix[row1-1][col2]
        left = self.sum_matrix[row2][col1-1]
        prefix = self.sum_matrix[row2][col2]
        #Need to add back cor since top and left overlaps here
        #so we substracted twice
        cor = self.sum_matrix[row1-1][col1-1]
        return prefix - top - left + cor
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)