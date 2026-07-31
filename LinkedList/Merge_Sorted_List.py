# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        all_elements = []

        head_1 = list1
        head_2 = list2
        if (head_1 is None) and (head_2 is None):
            return None

        curr = head_1

        while curr is not None:
            all_elements.append(curr.val)
            curr = curr.next

        curr = head_2

        while curr is not None:
            all_elements.append(curr.val)
            curr = curr.next

        all_elements.sort()

        head = ListNode(all_elements[0])

        curr = head

        for element in all_elements[1:]:
            new_node = ListNode(element)
            curr.next = new_node
            curr = new_node

        return head

        
        

        
            





        

        




        
