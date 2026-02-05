class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        num_1 = {}
        num_2 = {}

        for i in range(len(list1)):
            num_1[list1[i]] = i

        for i in range(len(list2)):
            num_2[list2[i]] = i

        mins = float("inf")

        for s in num_1:
            if s in num_2:
                mins = min(mins, num_1[s] + num_2[s])
        result = []
        for s in num_1:
            if s in num_2 and num_1[s] + num_2[s] == mins:
                result.append(s)

        return result

        
        