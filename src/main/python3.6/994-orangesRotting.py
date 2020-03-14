# -*- coding: UTF-8 -*-
# 开发团队： xx科技
# 开发人员： lee
# 创建时间： 2/25/20 10:59 PM
# 文件名称： a.py
# 开发工具： PyCharm

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        # 腐烂集合 {
        rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        # 新鲜集合
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        time = 0
        four_direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while fresh:
            if not rotten:
                return -1
            # 即将腐烂的如果在新鲜的集合中，就将它腐烂
            rotten = {(i + di, j + dj) for i, j in rotten for di, dj in four_direction
                      if (i + di, j + dj) in fresh}
            # 剔除腐烂的
            fresh -= rotten
            time += 1
        return time


solution = Solution()
time1 = solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(time1)
time2 = solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
print(time2)
time3 = solution.orangesRotting([[0, 2]])
print(time3)
