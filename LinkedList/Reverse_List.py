# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if (head is None):
            return None
        
        prev = None
        
        curr = head
        

        while curr is not None:
            temp_pointer = curr.next
            curr.next = prev
            prev = curr
            curr = temp_pointer

        
        return prev


