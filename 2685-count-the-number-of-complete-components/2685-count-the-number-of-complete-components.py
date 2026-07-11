from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node, component):
            visited[node] = True
            component.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, component)

        for i in range(n):

            if not visited[i]:

                component = []
                dfs(i, component)

                nodes = len(component)

                degree_sum = 0
                for node in component:
                    degree_sum += len(graph[node])

                actual_edges = degree_sum // 2
                expected_edges = nodes * (nodes - 1) // 2

                if actual_edges == expected_edges:
                    ans += 1

        return ans