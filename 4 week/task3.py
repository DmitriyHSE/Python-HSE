'''
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/merge-intervals/
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        listik = []
        for num in intervals:
            if not listik or listik[-1][1] < num[0]:
                listik.append(num)
            else:
                listik[-1][1] = max(listik[-1][1], num[1])

        return listik
