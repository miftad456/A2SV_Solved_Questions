class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = 0

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row, col):
            grid[row][col] = "0"  # mark visited

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if inbound(new_row, new_col) and grid[new_row][new_col] == "1":
                    dfs(new_row, new_col)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    island += 1   # count new island
                    dfs(i, j)

        return island