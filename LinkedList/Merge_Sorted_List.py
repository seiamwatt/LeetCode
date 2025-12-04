# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        all_elements = []

        head_list1 = list1
        head_list2 = list2

        curr_1 = head_list1
        curr_2 = head_list2

        while curr_1 is not None:
            all_elements.append(curr_1.val)
            curr_1 = curr_1.next

        while curr_2 is not None:
            all_elements.append(curr_2.val)
            curr_2 = curr_2.next

        all_elements.sort()

        dummy = ListNode(0)
        current = dummy


        for element in all_elements:
            current.next = ListNode(element)
            current = current.next

        return dummy.next

        






        
