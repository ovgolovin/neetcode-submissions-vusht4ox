# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class NodeWrap:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = dummy = ListNode()

        front = [NodeWrap(lst) for lst in lists if lst is not None]
        heapq.heapify(front)

        while front:
            node_wrap = heapq.heappop(front)
            curr.next = ListNode(node_wrap.node.val)
            curr = curr.next
            lst = node_wrap.node.next
            if lst:
                heapq.heappush(front, NodeWrap(lst))

        return dummy.next
        