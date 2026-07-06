from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        end = 0

        for start, finish in intervals:
            if finish > end:
                count += 1
                end = finish

        return count