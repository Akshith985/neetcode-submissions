# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        # Keep going if l1 exists, OR l2 exists, OR there is a leftover carry
        while l1 or l2 or carry:
            # Get values (use 0 if a list has already ended)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # New digit sum
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            
            # Create the node and move our pointer
            curr.next = ListNode(val)
            curr = curr.next
            
            # Move l1 and l2 forward if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next