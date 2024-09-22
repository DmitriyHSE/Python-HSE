'''
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, long = 0, 0
        ind = {}
        for i in range(len(s)):
            if s[i] in ind and ind[s[i]] >= start:
                start = ind[s[i]] + 1
            ind[s[i]] = i
            long = max(long, i - start + 1)
        return long