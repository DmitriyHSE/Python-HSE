'''
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/sliding-window-maximum/
'''

from collections import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        max_in_windows = []
        q = deque()
        for i in range(len(nums)):
            if q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                max_in_windows.append(nums[q[0]])

        return max_in_windows
