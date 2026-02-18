class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        new_arr =  copy.deepcopy(heights)
        my_dict  = {}
        for i in range(len(heights)):
            my_dict[heights[i]]  =  names[i]
        for i in range(len(new_arr)):
            for j in range(i+1,len(new_arr)):

                if new_arr[i] < new_arr[j]:
                    new_arr[j],new_arr[i]  =  new_arr[i],new_arr[j]
        result   = []
        for i in new_arr:
            result.append(my_dict[i])
        return result


        