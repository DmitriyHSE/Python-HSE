'''
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/permutations/
'''

from itertools import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, permutations(nums)))
