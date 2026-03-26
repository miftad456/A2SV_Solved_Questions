class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
      
     
        unfairness = float("inf")
        childs = [0] * k

        def backtrack(idx):
            nonlocal unfairness

            
            if idx == len(cookies):
                unfairness = min(unfairness, max(childs))
                return
            
            for i in range(k):
            
                childs[i] += cookies[idx]
                if max(childs) < unfairness:
                    backtrack(idx + 1)
                childs[i] -= cookies[idx]

        backtrack(0)
        return unfairness
                