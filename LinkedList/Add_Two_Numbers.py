# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []

        curr1 = l1 
        curr2 = l2

        while curr1 is not None:
            num1.append(curr1.val)
            curr1 = curr1.next

        while curr2 is not None:
            num2.append(curr2.val)
            curr2 = curr2.next


        num1.reverse()
        num2.reverse()

        number1 = ""
        number2 = ""

        for element in num1:
            number1 += str(element)
        
        for element in num2:
            number2 += str(element)


        sum = int(number1) + int(number2)
#  ''.join(reversed(s))
        dummy = ListNode(0)
        curr = dummy
        for element in ''.join(reversed(str(sum))):
            curr.next = ListNode(int(element))
            curr = curr.next

        return dummy.next



        

