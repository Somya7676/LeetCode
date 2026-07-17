from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        mx = max(nums)

        freq = [0] * (mx + 1)

        for x in nums:
            freq[x] += 1

        cnt = [0] * (mx + 1)

        for d in range(1, mx + 1):
            for m in range(d, mx + 1, d):
                cnt[d] += freq[m]

        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):

            total = cnt[d] * (cnt[d] - 1) // 2

            k = d * 2

            while k <= mx:
                total -= exact[k]
                k += d

            exact[d] = total

        prefix = []
        values = []

        s = 0

        for g in range(1, mx + 1):
            if exact[g]:
                s += exact[g]
                prefix.append(s)
                values.append(g)

        ans = []

        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans