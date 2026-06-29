# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy
        
        for _ in range(left - 1):
            pre = pre.next

        curr = pre.next
        nxt = curr.next
        for _ in range(right - left):
            nxt_nxt = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = nxt_nxt

        pre.next.next = nxt
        pre.next = curr

        return dummy.next


        

        

        