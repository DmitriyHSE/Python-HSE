'''
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-repeating-character-replacement/
'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        listik = [0] * 26
        left = 0
        count = 0
        length = 0
        for right in range(len(s)):
            listik[ord(s[right]) - ord('A')] += 1
            count = max(count, listik[ord(s[right]) - ord('A')])
            while (right - left + 1) - count > k:
                listik[ord(s[left]) - ord('A')] -= 1
                left += 1
            length = max(length, right - left + 1)

        return length
