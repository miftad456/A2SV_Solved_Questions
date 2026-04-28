class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        direction = [(0 , 1)  ,(0, -1) , (1, 0) ,(-1 , 0)]
        count   = 0 
        for i in range(rows):
            for j in range(cols):
                if grid [i][j] == "1":
                    count += 1

                    stack = [( i ,j)]
                    while stack:
                        row   ,col  = stack.pop()

                        if (row  < 0 or col < 0 or row  >= rows or col >= cols or grid[row][col] == "0"):
                            continue
                        
                        grid[row][col]  = "0"

                        for dr , dc  in direction:
                            stack.append((dr +  row  , dc + col ))
                        
                        
        return count
