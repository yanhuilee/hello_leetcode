# -*- coding: UTF-8 -*-
# 开发团队： xx科技
# 开发人员： lee
# 创建时间： 3/14/20 4:08 PM
# 文件名称： 300-最长上升子序列
# 给定一个无序的整数数组，找到其中最长上升子序列的长度

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 存储最长子序列
        serial = []
        for num in nums:
            if not serial or num > serial[-1]:
                serial.append(num)
                continue
            # 二分查找子序列中 num 的合适位置 location
            left, right = 0, len(serial) - 1
            location = right
            while left <= right:
                mid = (left + right) // 2
                if serial[mid] >= num:
                    location = mid
                    right = mid - 1
                else:
                    left = mid + 1
            serial[location] = num
        print(serial)
        return len(serial)

solution = Solution()
print(solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
# [1, 3, 4, 5, 6, 10] 根本不是最长子序列？？
