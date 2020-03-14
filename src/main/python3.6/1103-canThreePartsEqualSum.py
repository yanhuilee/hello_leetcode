# -*- coding: UTF-8 -*-
# 开发团队： xx科技
# 开发人员： lee
# 创建时间： 3/11/20 12:06 PM
# 文件名称： 1013. 将数组分成和相等的三个部分

from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_A = sum(A)
        # 都是整数，不可能有小数
        if sum_A % 3 != 0:
            return False
        target = sum_A // 3
        i, sum_curr, n = 0, 0, len(A)
        while i < n:
            sum_curr += A[i]
            if sum_curr == target:
                break
            i += 1

        j = i + 1
        while j + 1 < n:
            sum_curr += A[j]
            if sum_curr == target * 2:
                return True
            j += 1
        return False


if __name__ == '__main__':
    A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    solution = Solution()
    result = solution.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4])
    print(result)
