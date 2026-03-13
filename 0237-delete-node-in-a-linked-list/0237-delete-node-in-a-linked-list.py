# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        cur=node.next
        tem=cur.next
        node.next=tem
        node.val=cur.val
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        