class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if(head is None):
            return None
        
        curr = head
        length = 0
        prev = None
        index = 0
        null_pointer = None

        while(curr is not None):

            length += 1
            curr = curr.next

        
        remove_index = (length - n) 

        if(remove_index == 0):
            head = head.next
            return head


        curr = head
        prev = None
        index = 0

        while(curr is not None):
            #   a -> b -> c

            if(index == remove_index):
               next_node = curr.next
               prev.next = next_node 
               break
               

            prev = curr
            curr = curr.next
            index += 1


        return head
            











        

