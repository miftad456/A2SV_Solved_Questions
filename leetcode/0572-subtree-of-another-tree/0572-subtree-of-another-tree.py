# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, mainRoot, subRoot):
        
        def isIdentical(nodeA, nodeB):
            if not nodeA and not nodeB:
                return True
            if not nodeA or not nodeB:
                return False
            if nodeA.val != nodeB.val:
                return False
            
            return (isIdentical(nodeA.left, nodeB.left) and 
                    isIdentical(nodeA.right, nodeB.right))
        
        def dfs(current):
            if not current:
                return False
            
            if current.val == subRoot.val and isIdentical(current, subRoot):
                return True
            
            return dfs(current.left) or dfs(current.right)
        
        return dfs(mainRoot)   