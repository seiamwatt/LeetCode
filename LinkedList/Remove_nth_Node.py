class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        list_len = 0

        curr_node = head

        while curr_node is not None:
            list_len += 1
            curr_node = curr_node.next
           

        remove_index = list_len - n -1

        curr_node = head
        dummy_node = ListNode(0,head)
        index = 0

        if list_len == 1:
            dummy_node = ListNode(0,None)
            return dummy_node.next
        
        if remove_index == 0:
            temp = curr_node.next.next

            next_node = curr_node.next
            next_node.next = None
            curr_node.next = temp

            return head
        
        if remove_index == -1:
            dummy_node.next = head.next
            return dummy_node.next
    
        while curr_node is not None:

            if index == remove_index:
                temp = curr_node.next.next

                next_node = curr_node.next
                next_node.next = None
                curr_node.next = temp 
            index += 1
            curr_node = curr_node.next

        return dummy_node.next






















        

