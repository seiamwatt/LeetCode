# Definition for singly-linked list.
# class ListNode:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head 
        prev_node = None

        while curr_node is not None:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp

        return prev_node





        # 1 -> 2 -> 3
        # 1 <- 2 <- 3 
      
    




