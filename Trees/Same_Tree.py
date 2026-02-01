# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.BFS(p) == self.BFS(q)
    
    def BFS(self, root: Optional[TreeNode]):
        if root is None:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node is None:
                result.append(None)
                continue  
            
            result.append(node.val) 
            
            queue.append(node.left)
            queue.append(node.right)
        
        return result  



        



        


        


        









