class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        node_list = []

        while curr is not None:

            if curr not in node_list:
                node_list.append(curr)
            elif curr in node_list:
                return True
            
            curr = curr.next
        return False