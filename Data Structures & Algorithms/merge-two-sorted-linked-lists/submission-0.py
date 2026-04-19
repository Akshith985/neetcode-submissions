# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to simplify the start
        dummy = ListNode()
        tail = dummy
        
        # 2. Iterate while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next # Move list1 pointer
            else:
                tail.next = list2
                list2 = list2.next # Move list2 pointer
            
            # Move the tail of our new list forward
            tail = tail.next
            
        # 3. If one list is finished, append the remainder of the other
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # 4. Return the actual head (which is after the dummy)
        return dummy.next