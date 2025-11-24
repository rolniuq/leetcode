#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

from typing import List
from collections import defaultdict, deque


# @lc code=start
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        visited = set()
        queue = deque([0])
        visited.add(0)
        changes = 0

        while queue:
            city = queue.popleft()

            for neighbor, cost in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    changes += cost

        return changes


# @lc code=end
