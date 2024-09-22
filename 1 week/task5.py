'''
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/wildcard-matching/
'''
import fnmatch


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        flag = fnmatch.fnmatch(s, p)
        return flag