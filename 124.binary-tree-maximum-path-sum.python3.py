# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_one_side(node):
            if not node:
                return 0
            left = max(0, max_one_side(node.left))
            right = max(0, max_one_side(node.right))
            self.ans = max(self.ans, node.val + left + right)
            return node.val + max(left, right)
        self.ans = -sys.maxsize
        max_one_side(root)
        return self.ans
