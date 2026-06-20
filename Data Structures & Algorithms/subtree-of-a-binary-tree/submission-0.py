# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            left_match = isSameTree(p.left,q.left)
            right_match = isSameTree(p.right,q.right)
            return left_match and right_match
        
        if not root:
            return False
        if isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)