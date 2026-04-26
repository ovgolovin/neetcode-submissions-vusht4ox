"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next
        
        curr = head
        while curr:
            curr.next.random = None if curr.random is None else curr.random.next
            curr = curr.next.next

        
        dummy = Node(0)
        curr = head
        copy = dummy
        while curr:
            copy.next = curr.next
            curr.next = curr.next.next
            curr = curr.next
            copy = copy.next

        return dummy.next
        
        