
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        

        if not root:
            return False
        
        if self.sameTree(root,subRoot):
            return True
        

        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
       

    def sameTree(self,tree1:Optional[TreeNode],tree2:Optional[TreeNode]):

        return self.BFS(tree1) == self.BFS(tree2)


        
    
    def BFS(self, root: Optional[TreeNode]):

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

        