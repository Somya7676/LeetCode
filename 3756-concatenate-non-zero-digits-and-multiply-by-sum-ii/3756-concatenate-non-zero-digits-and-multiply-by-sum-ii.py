from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        pos = []
        digit = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digit.append(int(ch))

        m = len(digit)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix number
        prefNum = [0] * (m + 1)
        for i in range(m):
            prefNum[i + 1] = (prefNum[i] * 10 + digit[i]) % MOD

        # prefix digit sum
        prefSum = [0] * (m + 1)
        for i in range(m):
            prefSum[i + 1] = prefSum[i] + digit[i]

        ans = []

        for l, r in queries:

            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (
                prefNum[right + 1]
                - prefNum[left] * pow10[length]
            ) % MOD

            sm = prefSum[right + 1] - prefSum[left]

            ans.append((x * sm) % MOD)

        return ans