'''
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        q = deque()
        q.append(root)
        while q:
            num = len(q)
            level = []
            for i in range(len(q)):
                x = q.popleft()
                if x:
                    level.append(x.val)
                    q.append(x.left)
                    q.append(x.right)
            if level:
                levels.append(level)
        for i in range(1, len(levels), 2):
            levels[i] = levels[i][::-1]

        return levels
