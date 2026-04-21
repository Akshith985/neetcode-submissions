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
        # Map to store {OriginalNode: CopiedNode}
        # We include None: None to handle the end of the list
        old_to_copy = {None: None}
        
        # 1st Pass: Create all the new nodes (clones)
        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_copy[curr] = copy
            curr = curr.next
            
        # 2nd Pass: Connect the pointers
        curr = head
        while curr:
            copy = old_to_copy[curr]
            # Point the copy's next to the map's version of the original's next
            copy.next = old_to_copy[curr.next]
            # Point the copy's random to the map's version of the original's random
            copy.random = old_to_copy[curr.random]
            curr = curr.next
            
        return old_to_copy[head]