# -*- coding: UTF-8 -*-
# 开发团队： xx科技
# 开发人员： lee
# 创建时间： 3/8/20 8:32 PM
# 文件名称： xx.py

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        res = 0
        profit = [[0 for i in range(3)] for i in range(len(prices))]
        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0

        for i in range(1, len(prices)):
            profit[i][0] = profit[i - 1][0]
            profit[i][1] = max(profit[i - 1][1], profit[i - 1][0] - prices[i])
            profit[i][2] = profit[i - 1][1] + prices[i]
            res = max(res, profit[i][0], profit[i][1], profit[i][2])
        return res
