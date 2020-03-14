# -*- coding: UTF-8 -*-
# 开发团队： xx科技
# 开发人员： lee
# 创建时间： 3/6/20 12:14 PM
# 文件名称： 57-findContinuousSequence.py

from typing import List
from time import time


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 除会向下取整要加1，range 右边是闭区间，因此是加2
        num_list = list(range(1, target // 2 + 2))
        sequence = []
        left, right = 0, 2
        circle = 0
        while left < right < num_list[-1] + 1:
            circle += 1
            sum_current = sum(num_list[left:right])
            print("sum_current = ", sum_current)
            if sum_current > target:
                left += 1
                continue
            elif sum_current == target:
                sequence.append(num_list[left:right])
                left += 1
            right += 1
        print("循环了", circle)
        return sequence


start = time()
solution = Solution()
result = solution.findContinuousSequence(87760)
# result = solution.findContinuousSequence(15)
# result = solution.findContinuousSequence(14)
print(result, "runtime is : ", time() - start)

