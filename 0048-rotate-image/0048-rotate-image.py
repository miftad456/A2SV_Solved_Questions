class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        response = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            matrix[i].clear()
        print(matrix)

        for i in range(len(response)):
                for j in range(len(response[0])):
                    matrix[j].append(response[i][j])
        for i in  range(len(matrix)):
            matrix[i]  = matrix[i][::-1]

            
        """
        Do not return anything, modify matrix in-place instead.
        """
        