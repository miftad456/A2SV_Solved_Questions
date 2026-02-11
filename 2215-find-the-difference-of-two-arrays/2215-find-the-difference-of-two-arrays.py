class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        array1 =  list(set(nums1) - set(nums2))
        array2 = list(set(nums2) - set(nums1))
        return [array1,array2] 
        