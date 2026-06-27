from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)

        ans = 1

        if 1 in freq:
            if freq[1] % 2 == 0:
                ans = freq[1] - 1
            else:
                ans = freq[1]

        for x in list(freq.keys()):

            if x == 1:
                continue

            length = 0
            curr = x

            while curr in freq and freq[curr] >= 2:

                length += 2
                curr = curr * curr

            if curr in freq:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans