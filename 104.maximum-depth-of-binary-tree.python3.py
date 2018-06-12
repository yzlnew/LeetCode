# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        queue = [root]
        while root and queue:
            depth += 1
            queue = [child for node in queue for child in
                     (node.left, node.right) if child]
        return depth
