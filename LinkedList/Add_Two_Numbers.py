from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr_node = l1
        temp1 = ""

        while curr_node is not None:
            temp1 += str(curr_node.val)
            curr_node = curr_node.next

        curr_node = l2
        temp2 = ""

        while curr_node is not None:
            temp2 += str(curr_node.val)
            curr_node = curr_node.next

        num1  = temp1[::-1]
        num2 = temp2[::-1]

        total = int(num1) + int(num2)
        str_total = str(total)

        output = []
        for number in str_total[::-1]:
            output.append(int(number))

        dummy = ListNode()
        curr_node = dummy

        for num in output:
            curr_node.next = ListNode(num)
            curr_node = curr_node.next


        return dummy.next



def build_linked_list(nums):
    dummy = ListNode()
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


def print_linked_list(node):
    values = []
    while node is not None:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))


def main():
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result)


if __name__ == "__main__":
    main()