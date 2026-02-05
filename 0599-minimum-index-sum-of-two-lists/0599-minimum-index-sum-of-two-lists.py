class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        num_1   = {}
        num_2   =   {}
        for i in range(len(list1)):
            num_1[list1[i]]  = i
        for i in range(len(list2)):
            num_2[list2[i]]  = i
        mins =  float("inf")
        for i in num_1:
            if i in num_2:
                mins  = min(mins,num_1[i]+num_2[i])
        result  = []
        for i in num_1:
            if num_1[i] ==mins and i in num_2 :
                result.append(i)
        for i in num_2:
            if num_2[i] ==mins and i  in num_1:
                result.append(i)
        return result

        
        