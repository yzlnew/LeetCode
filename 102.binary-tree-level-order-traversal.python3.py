# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, queue = [], [root]

        while queue and root:
            ans.append([node.val for node in queue])
            queue = [child for node in queue for child in
                     (node.left, node.right) if child]

        return ans
