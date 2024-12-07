'''
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/recover-binary-search-tree/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inorder(root):
            if root:
                return inorder(root.left) + [root] + inorder(root.right)
            else:
                return []

        lst = inorder(root)
        pt1 = None
        prev = lst[0].val
        for node in lst:
            if prev > node.val:
                pt1 = node
            prev = node.val
        for node in lst:
            if pt1.val < node.val:
                pt1.val, node.val = node.val, pt1.val
                break
