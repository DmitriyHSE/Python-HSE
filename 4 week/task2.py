'''
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/permutations-ii/
'''

from itertools import *


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, set(permutations(nums))))
