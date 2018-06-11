# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            vals = [node.val if node else None for node in queue]
            if vals != vals[::-1]:
                return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True
