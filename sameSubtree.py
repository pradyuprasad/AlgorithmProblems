# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return not subRoot
        if not subRoot:
            return not root
        if root.val == subRoot.val:
            return self.isSameTree(root, subRoot) 
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if not t1:
            return not t2
        if not t2:
            return not t1
        
        if t1.val != t2.val:
            return False
        
        return self.isSameTree(t1.right, t2.right) and self.isSameTree(t1.left, t2.left)