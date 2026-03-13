class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr  = sorted(costs , key  = lambda x: x[0] -  x[1])
        res =  0
        for i in range(len(costs)):
            if i <  len(costs) // 2:
                res += arr[i][0]
            else:
                res +=  arr[i][1]
        return res 

        