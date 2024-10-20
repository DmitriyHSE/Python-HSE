'''
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/4sum-ii/
'''

from collections import *


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        sum_count = defaultdict(int)
        for a in nums1:
            for b in nums2:
                sum_count[a + b] += 1
        for c in nums3:
            for d in nums4:
                count += sum_count[-(c + d)]

        return count
