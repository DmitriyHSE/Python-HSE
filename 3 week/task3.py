'''
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/maximum-subarray/
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = nums[0]
        result = nums[0]
        for num in nums[1:]:
            sums = max(num, sums + num)
            result = max(result, sums)

        return result
