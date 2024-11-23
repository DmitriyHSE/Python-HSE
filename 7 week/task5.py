'''
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/max-consecutive-ones-iii/
'''


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_len = max(max_len, i - left + 1)

        return max_len
