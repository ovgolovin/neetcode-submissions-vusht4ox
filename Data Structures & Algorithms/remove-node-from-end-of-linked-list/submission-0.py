# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        peek = head
        for _ in range(n):
            peek = peek.next
        curr = dummy
        while peek:
            curr = curr.next
            peek = peek.next
        curr.next = curr.next.next
        return dummy.next
        