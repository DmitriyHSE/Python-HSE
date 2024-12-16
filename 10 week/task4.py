'''
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            level = []
            for i in range(len(q)):
                n = q.pop(0)
                level.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            ans.append(level)
        ans.reverse()

        return ans
