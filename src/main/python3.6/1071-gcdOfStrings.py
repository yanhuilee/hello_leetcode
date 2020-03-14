# -*- coding: UTF-8 -*-
# 开发团队： xx科技
# 开发人员： lee
# 创建时间： 3/12/20 12:03 PM
# 文件名称： 1071-字符串的最大公因子

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 求 len(str2) 和 len(str2) 的最大公约数candidate
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[:candidate_len]
        if str1 + str2 == str2 + str1:
            return candidate
        return ""
