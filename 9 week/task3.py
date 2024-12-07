'''
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/validate-binary-search-tree/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mn, mx = float('-inf'), float('inf')

        def check(root, mn, mx):
            if root == None:
                return True
            if root.val <= mn or root.val >= mx:
                return False
            return check(root.left, mn, root.val) and check(root.right, root.val, mx)

        return check(root, mn, mx)
