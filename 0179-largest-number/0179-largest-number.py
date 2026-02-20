class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        newarr=list(map(str,nums))
        newarr.sort(key=lambda x:x*10 ,reverse=True)
        if newarr[0]=="0":
            return "0"
        g="".join(newarr)
        return g
        