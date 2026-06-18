# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def rec(head: Optional[ListNode], prev: Optional[ListNode]) -> ListNode:
    if head is None:
        return prev
    next_node = head.next
    head.next = prev
    return rec(next_node, prev=head)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return rec(head, prev=None)
        