'''
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        str, palindrom = '', ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j] and s[i:j] == s[j:i:-1]:
                    str = s[i:j + 1]
                    if len(str) > len(palindrom):
                        palindrom = str
        return palindrom
