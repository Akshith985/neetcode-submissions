# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_so_far = root
        queue = deque([(root, root.val)])
        res = 0
        while queue:
            node, max_so_far = queue.popleft()
            if node.val >= max_so_far:
                res+=1
            new_max = max(max_so_far, node.val)
            if node.left:
                queue.append((node.left,new_max))
            if node.right:
                queue.append((node.right,new_max))
        return res