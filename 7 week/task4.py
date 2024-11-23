'''
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-turbulent-subarray/
'''


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
        max_len = 1
        current_len = 1
        last_relation = 0
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                current_relation = 1
            elif arr[i] < arr[i - 1]:
                current_relation = -1
            else:
                current_relation = 0
            if current_relation == 0:
                current_len = 1
            elif last_relation * current_relation < 0:
                current_len += 1
            else:
                current_len = 2
            max_len = max(max_len, current_len)
            last_relation = current_relation

        return max_len
