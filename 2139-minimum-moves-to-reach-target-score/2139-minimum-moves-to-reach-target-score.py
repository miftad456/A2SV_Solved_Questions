class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move  = 0
        while maxDoubles > 0 and target > 1: 
            if target % 2 ==1:
                move += 1
                target -= 1
                print(move)
            else:
                move += 1
                target //= 2
                maxDoubles -= 1
                
        if target > 1:
            move += target -  1
        return move

        