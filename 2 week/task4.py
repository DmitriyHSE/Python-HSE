"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/word-break-ii/
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]
            results = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for sub_sentence in backtrack(end):
                        if sub_sentence:
                            results.append(word + " " + sub_sentence.strip())
                        else:
                            results.append(word)
            memo[start] = results
            return results

        return backtrack(0)
