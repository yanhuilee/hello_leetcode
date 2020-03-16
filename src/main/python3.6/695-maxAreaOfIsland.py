# -*- coding: UTF-8 -*-
# 开发团队： xx科技
# 开发人员： lee
# 创建时间： 3/14/20 4:08 PM
# 文件名称： 695-岛屿的最大面积
# 给定一个包含了一些 0 和 1的非空二维数组 grid ,
# 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for idx, line in enumerate(grid):
            for j, n in enumerate(line):
                ans = max(self.dfs(grid, idx, j), ans)
        return ans

    def dfs(self, grid, cur_i, cur_j):
        print("cur_i = ", cur_i, " cur_j = ", cur_j)
        if cur_i < 0 or cur_j < 0 \
                or cur_i == len(grid) or cur_j == len(grid[0]) \
                or grid[cur_i][cur_j] != 1:
            return 0

        # 为了确保每个土地访问不超过一次，我们每次经过一块土地时，将这块土地的值置为 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans


solution = Solution()
A = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
print(solution.maxAreaOfIsland(A))
