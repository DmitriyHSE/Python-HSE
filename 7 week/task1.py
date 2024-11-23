'''
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-k-closest-elements/
'''


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        while right - left >= k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1

        return arr[left:left + k]
