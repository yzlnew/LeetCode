# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, queue = [], [root]
        level = 0

        while root and queue:
            new_vals = [node.val for node in queue]
            level = level ^ 1

            if level == 1:
                ans.append(new_vals)
            else:
                ans.append(new_vals[::-1])
            queue = [child for node in queue for child in
                     (node.left, node.right) if child]

        return ans
