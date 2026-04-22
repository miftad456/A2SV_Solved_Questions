class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows  , cols  =  len(grid)  , len(grid[0])
        direction  = [(0 , 1) , (0 , -1) , (1,0) ,(-1 , 0)]

        visited  = [[False for i in range(cols)] for j in range(rows)]
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(grid , visited , row , col):

            visited[row][col]  = True
            perimetir  = 0

            for row_c ,  col_c in direction:
                new_row =  row +  row_c
                new_col  = col  + col_c
                if not  inbound(new_row  , new_col)  or grid[new_row][new_col] == False:
                    perimetir +=  1
                elif  inbound(new_row  , new_col) and not visited[new_row][new_col]:
                    perimetir +=  dfs(grid ,visited ,new_row , new_col)
            return perimetir 


        for  row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(grid , visited , row , col)
        return 0


        



        