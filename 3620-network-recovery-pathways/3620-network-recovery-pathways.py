from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = []

        for u, v, c in edges:
            graph[u].append((v, c))
            indegree[v] += 1
            costs.append(c)

        # Topological Order
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, c in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        if not costs:
            return -1

        costs = sorted(set(costs))

        def check(limit):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, c in graph[u]:
                    if c < limit:
                        continue
                    if v != n - 1 and v != 0 and not online[v]:
                        continue
                    if dist[u] + c < dist[v]:
                        dist[v] = dist[u] + c

            return dist[n - 1] <= k

        left, right = 0, len(costs) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if check(costs[mid]):
                ans = costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return ans