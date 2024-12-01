'''
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
'''


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        mx = -1
        sm = 0
        left = 0
        for right in range(len(nums)):
            sm += nums[right]
            while sm > target and left <= right:
                sm -= nums[left]
                left += 1
            if sm == target:
                mx = max(mx, right - left + 1)

        if mx == -1:
            return -1
        else:
            return len(nums) - mx
