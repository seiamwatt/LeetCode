from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr_node = head
        node_dict = {}

        while curr_node is not None:
            node_dict[curr_node] = Node(curr_node.val)
            curr_node = curr_node.next

        curr_node = head
        while curr_node is not None:
            temp_node = node_dict[curr_node]
            temp_node.next = node_dict.get(curr_node.next)
            temp_node.random = node_dict.get(curr_node.random)
            curr_node = curr_node.next

        return node_dict[head]






        
            
            
        