'''
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/burst-balloons/submissions/
'''


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        dp = [[0] * len(arr) for i in range(len(arr))]
        for length in range(2, len(arr)):
            for left in range(len(arr) - length):
                right = left + length
                for i in range(left + 1, right):
                    coins = arr[left] * arr[i] * arr[right]
                    total = coins + dp[left][i] + dp[i][right]
                    dp[left][right] = max(dp[left][right], total)

        return dp[0][len(arr) - 1]
