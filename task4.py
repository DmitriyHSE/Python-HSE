'''
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-valid-parentheses/
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        long = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    long = max(long, i - stack[-1])

        return long