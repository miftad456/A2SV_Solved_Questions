class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        res=[]
        for i in d:
            if d[i]>len(nums)//3:
                res.append(i)
        return res
        