'''
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx = float('-inf')
        self.maxSum(root, self.mx)
        return self.mx

    def maxSum(self, root, maxs):
        if root is None:
            return 0
        ls = max(0, self.maxSum(root.left, self.mx))
        rs = max(0, self.maxSum(root.right, self.mx))
        self.mx = max(self.mx, root.val + ls + rs)
        return root.val + max(ls, rs)
