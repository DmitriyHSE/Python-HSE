'''
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/grumpy-bookstore-owner/
'''


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total, mx, cur = 0, 0, 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total += customers[i]
        for i in range(len(customers)):
            if grumpy[i] == 1:
                cur += customers[i]
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    cur -= customers[i - minutes]
            if i >= minutes - 1:
                mx = max(mx, cur)

        return total + mx
