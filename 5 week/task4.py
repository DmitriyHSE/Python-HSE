'''
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/fraction-to-recurring-decimal/
'''


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part = numerator // denominator
        remainder = numerator % denominator
        if remainder == 0:
            return f"{sign}{integer_part}"
        fractional_part = ""
        remainder_map = {}
        index = 0
        while remainder != 0:
            if remainder in remainder_map:
                start_index = remainder_map[remainder]
                non_repeating = fractional_part[:start_index]
                repeating = fractional_part[start_index:]
                return f"{sign}{integer_part}.{non_repeating}({repeating})"
            remainder_map[remainder] = index
            remainder *= 10
            fractional_part += str(remainder // denominator)
            remainder %= denominator
            index += 1

        return f"{sign}{integer_part}.{fractional_part}"
