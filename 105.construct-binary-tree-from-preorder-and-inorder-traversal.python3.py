# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if preorder:
            root = TreeNode(preorder[0])
            root_index = inorder.index(root.val)
            root.left = self.buildTree(
                preorder[1:1 + root_index], inorder[:root_index])
            root.right = self.buildTree(
                preorder[1 + root_index:], inorder[root_index + 1:])
            return root

        return None
