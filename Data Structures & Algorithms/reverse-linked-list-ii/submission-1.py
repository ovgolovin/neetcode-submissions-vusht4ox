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

        prev = None
        curr = pre.next
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            

        pre.next.next = curr
        pre.next = prev

        return dummy.next


        

        

        