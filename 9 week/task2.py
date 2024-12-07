'''
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees-ii/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gen(i, start):
            if i == 0:
                return [None]
            if i == 1:
                return [TreeNode(i + start)]
            res = list()
            for j in range(i):
                left = list(gen(j, start))
                right = list(gen(i - 1 - j, start + j + 1))
                for l in left:
                    for r in right:
                        root = TreeNode(start + j + 1)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        return gen(n, 0)
