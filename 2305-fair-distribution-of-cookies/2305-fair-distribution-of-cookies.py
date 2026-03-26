class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
      
     
        unfairness = float("inf")
        childs = [0] * k

        def backtrack(idx,max_so):
            nonlocal unfairness

            
            if idx == len(cookies):
                unfairness = min(unfairness, max(childs))
                return
            for i in range(k):
            
                childs[i] += cookies[idx]
                if max(childs) < unfairness:
                    backtrack(idx + 1,max(max_so ,max(childs)))
                childs[i] -= cookies[idx]
                if childs[i] == 0 :
                    return 

        backtrack(0,0)
        return unfairness
                