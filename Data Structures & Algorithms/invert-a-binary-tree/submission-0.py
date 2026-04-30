# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. Base Case: If the tree is empty, we're done
        if not root:
            return None
        
        # 2. Swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # 3. Recursively call the function on the children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 4. Return the root of the now-inverted tree
        return root