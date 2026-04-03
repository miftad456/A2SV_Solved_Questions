class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def get_winner(n, k):
            if n==0:
                return 0
            return (get_winner(n-1,k )+  k ) % n
        return get_winner(n ,k) + 1
        