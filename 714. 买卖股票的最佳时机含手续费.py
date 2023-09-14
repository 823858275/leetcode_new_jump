from typing import List


# 可以类似以往的股票题目，设置几个状态，使用动态规划
# 贪心算法
# 如果股票一直涨，就获取收益，更新buy，相当于更新了现在的成本
# 如果跌了，并且超过了手续费，相当于股票清空，重新购买股票
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        buy = prices[0] + fee
        for i in range(1, len(prices)):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit
