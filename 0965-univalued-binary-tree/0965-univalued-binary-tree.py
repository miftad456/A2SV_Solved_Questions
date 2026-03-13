# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        visited  = set()
        queue  = deque()
        queue.append(root)
        while queue :
            curr  = queue.popleft()
            visited.add(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        if len(visited) <=  1:
            return True
        return False 





        