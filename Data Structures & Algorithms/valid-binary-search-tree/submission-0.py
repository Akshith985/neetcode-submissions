# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([(root, float("-inf"), float("inf"))])
        while queue:
            length = len(queue)
            node, left_wall, right_wall = queue.popleft()
            if node.val <= left_wall or node.val >= right_wall:
                return False
            if node.left:
                queue.append((node.left, left_wall, node.val))
            if node.right:
                queue.append((node.right, node.val, right_wall))
        return True
