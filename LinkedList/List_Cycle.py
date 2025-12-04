class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head 

        hash_map = {}
        index = 0

        if(curr is None):
            return False

        if(curr.next is None):
            return False
        
        

        while curr is not None:
            hash_map[curr] = True

            if(curr.next in hash_map):
                return True
            
            hash_map[curr] = True
            curr = curr.next

            
        return False