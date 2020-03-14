# -*- coding: UTF-8 -*-
# 开发团队： xx科技
# 开发人员： lee
# 创建时间： 3/8/20 12:06 AM
# 文件名称： 322-coinChange.py

from typing import List

class Solution:
    def coinChange2(self, coins: List[int], amount: int) -> int:
        coins_sort = list(reversed(coins))
        nums, max = 0, len(coins_sort) - 1
        results = []
        while amount > 0:
            if amount >= coins_sort[nums]:
                amount -= coins_sort[nums]
                results.append(coins_sort[nums])
            else:
                nums = (nums + 1) if nums < max else max
            if nums == max and amount < coins_sort[nums]:
                return -1
        print(results)
        return len(results)

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[-1] == amount + 1 else dp[-1]

    def coinChange3(self, coins: List[int], amount: int) -> int:
        max = amount + 1


solution = Solution()
# result = solution.coinChange(coins=[1, 2, 5], amount=11)

result = solution.coinChange(coins=[2], amount=3)
print(result)
