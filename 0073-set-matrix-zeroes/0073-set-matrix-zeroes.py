class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row  =  set()
        col =  set()
        for i  in  range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        print(row)
        print(col)

        for i in row:
            matrix[i] =  [0] * len(matrix[0])
        for c in col:
            for j in range(len(matrix)):
                matrix[j][c] =  0
        """
        Do not return anything, modify matrix in-place instead.
        """
        