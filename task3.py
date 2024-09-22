'''
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ''
        else:
            chars = {
                    '2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'
                }
            result = ['']
            for digit in digits:
                result = [comb + i for comb in result for i in chars[digit]]
            return result