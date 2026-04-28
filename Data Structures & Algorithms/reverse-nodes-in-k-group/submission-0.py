# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummy = ListNode(next=head)
        cur = dummy

        while True:
            new_last = cur
            for _ in range(k):
                new_last = new_last.next
                if new_last is None:
                    break
            if new_last is None:
                break

            new_head = cur.next
            
            prev = new_head
            tmp = prev.next
            for _ in range(k - 1):
                nxt = tmp.next
                tmp.next = prev
                prev = tmp
                tmp = nxt

            cur.next = prev
            new_head.next = tmp
            cur = new_head

        return dummy.next

        