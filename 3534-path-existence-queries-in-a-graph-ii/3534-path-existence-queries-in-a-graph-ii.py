from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        arr = sorted((v, i) for i, v in enumerate(nums))

        pos = [0] * n
        values = [0] * n

        for i, (v, idx) in enumerate(arr):
            pos[idx] = i
            values[i] = v

        # farthest reachable in one edge
        nxt = [0] * n
        r = 0

        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            nxt[l] = r

        LOG = 18

        up = [[0] * n for _ in range(LOG)]
        up[0] = nxt[:]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        ans = []

        for u, v in queries:

            if u == v:
                ans.append(0)
                continue

            l = pos[u]
            r = pos[v]

            if l > r:
                l, r = r, l

            if up[LOG - 1][l] < r:
                ans.append(-1)
                continue

            cur = l
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    steps += 1 << k
                    cur = up[k][cur]

            ans.append(steps + 1)

        return ans
        