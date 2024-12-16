'''
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/path-sum-ii/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int):
        if not root:
            return []
        stack = [(root, [root.val], targetSum - root.val)]
        result = []
        while stack:
            current_node, current_path, remaining_sum = stack.pop()
            if not current_node.left and not current_node.right and remaining_sum == 0:
                result.append(current_path)
            if current_node.right:
                stack.append((current_node.right, current_path + [current_node.right.val],
                              remaining_sum - current_node.right.val,))
            if current_node.left:
                stack.append(
                    (current_node.left, current_path + [current_node.left.val], remaining_sum - current_node.left.val,))

        return result
