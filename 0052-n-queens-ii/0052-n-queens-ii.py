class Solution:
    def totalNQueens(self, n: int) -> int:

        cols  =  [False] * n
        posdiag = [False] *(2*n -1)
        negdiag  =[False] *  (2  * n - 1)
        board = [["."] * n for _ in range(n)]
        print(board)
        result = []

        def backtrack(r):
            if r ==  n:
                result.append(["".join(row) for row in board])
                return
            for c in range(n):
                pos =  r - c
                neg =  r +  c
                if cols[c]  or posdiag[pos] or negdiag[neg]:
                    continue
                cols[c] = posdiag[pos] = negdiag[neg] =   True
                board[r][c]  =  "Q"
                backtrack(r +  1)
                cols[c] = posdiag[pos] = negdiag[neg] =   False
                board[r][c]  =  "."
        backtrack(0)
        return len(result)

                
                  

        