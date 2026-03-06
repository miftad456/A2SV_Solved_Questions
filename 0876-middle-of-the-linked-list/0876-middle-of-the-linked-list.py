# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp =  head
        length =  0
        while temp :
            temp =  temp.next
            length += 1
        middle  =  (length // 2) +  1
        if middle ==  1:
            return head
        curr =  head
        for i  in range(middle - 2):
            curr =  curr.next
        return curr.next
        