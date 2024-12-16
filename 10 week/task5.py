'''
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def sort(i, j):
            if i > j: return None
            mid = (i + j) // 2
            root = TreeNode(values[mid])
            root.left = sort(i, mid - 1)
            root.right = sort(mid + 1, j)
            return root

        return sort(0, len(values) - 1)
