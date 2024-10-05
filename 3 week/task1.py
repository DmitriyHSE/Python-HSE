'''
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/container-with-most-water/
'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(result, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result
