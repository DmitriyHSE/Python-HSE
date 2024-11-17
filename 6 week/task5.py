'''
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/binary-subarrays-with-sum/
'''


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        sum = 0
        prefix = {0: 1}
        for num in nums:
            sum += num
            if sum - goal in prefix:
                count += prefix[sum - goal]
            if sum in prefix:
                prefix[sum] += 1
            else:
                prefix[sum] = 1

        return count
