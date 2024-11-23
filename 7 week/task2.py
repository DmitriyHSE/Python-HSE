'''
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/subarray-product-less-than-k/
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        pr = 1
        count = 0
        left = 0
        for i in range(len(nums)):
            pr *= nums[i]
            while pr >= k:
                pr //= nums[left]
                left += 1
            count += i - left + 1

        return count
