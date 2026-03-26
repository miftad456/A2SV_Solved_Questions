# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        class Node:
            def __init__(self,data):
                self.left =  None
                self.right  = None
                self.data = data
        def tree(start , end):
            if start > end:
                return None
            mid  =  start + (end - start) // 2
            root =  TreeNode(nums[mid])

            root .left =  tree(start, mid-1)
            root.right  = tree(mid  + 1,end)

            return root
        return tree(0 , len(nums)-1)
            

        