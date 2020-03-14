# -*- coding: UTF-8 -*-
# 开发团队： xx科技
# 开发人员： lee
# 创建时间： 3/5/20 3:15 PM
# 文件名称： 1103-distributeCandies.py

from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # 每个人位置列表，在第n个位置表示等到n个糖果
        index_of_people = [person for person in range(1, num_people + 1)]
        print(index_of_people)

        # 每人分得糖果总数
        candy = [0 for i in range(num_people)]
        circle = 1
        while candies > 0:
            # 第 circle 需要的糖果总数
            sum_of_circles = int(num_people * (1 + num_people) * 0.5 + num_people * num_people * (circle - 1))
            print("sum_of_circles = ", sum_of_circles)
            if candies < sum_of_circles:
                break
            # 剩下的糖果够分一圈，直接减
            candies -= sum_of_circles
            # 新一圈每人需要的糖果数量
            candy_y = [(x + num_people * (circle - 1)) for x in index_of_people]
            # 每个人得到的糖果总数
            candy = [(candy[i] + candy_y[i]) for i in range(num_people)]
            circle += 1

        # 剩余糖果不够分一圈，从头一个个分
        for i in range(num_people):
            # 当前孩子本次需要的糖果数量
            candy_of_i = 1 + i + num_people * (circle - 1)
            print("i+1, candy_of_i = ", i + 1, candy_of_i)
            if candies > candy_of_i:
                candies -= candy_of_i
                candy[i] += candy_of_i
            else:
                candy[i] += candies
                # candies = 0
                break
        return candy


solution = Solution()
result = solution.distributeCandies(70, 4)
print(result)
# print("-" * 50)
# result2 = solution.distributeCandies(10, 3)
# print(result2)
# result3 = solution.distributeCandies(60, 4)
# print(result3)

