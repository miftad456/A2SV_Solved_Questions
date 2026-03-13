# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        array  = []
        queue =  deque()
        queue.append(root)
        if not root:
            return []
        while queue:
            n  = len(queue)
            res = []
            for i in range(n):
                curr  = queue.popleft()
                res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            array.append(res[:])
        return array

            

        