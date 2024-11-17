'''
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        len_s, len_p = len(s), len(p)
        if len_p > len_s:
            return []
        p_count = Counter(p)
        s_count = Counter(s[:len_p])
        if s_count == p_count:
            result.append(0)
        for i in range(len_p, len_s):
            s_count[s[i]] += 1
            s_count[s[i - len_p]] -= 1
            if s_count[s[i - len_p]] == 0:
                del s_count[s[i - len_p]]
            if s_count == p_count:
                result.append(i - len_p + 1)

        return result
