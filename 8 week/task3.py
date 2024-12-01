'''
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/get-equal-substrings-within-budget/
'''


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, total, mx = 0, 0, 0
        for right in range(len(s)):
            total += abs(ord(s[right]) - ord(t[right]))
            while total > maxCost:
                total -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            mx = max(mx, right - left + 1)

        return mx