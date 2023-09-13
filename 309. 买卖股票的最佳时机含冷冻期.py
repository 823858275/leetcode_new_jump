from typing import List


# f[i] 为第i天累计收益
# 设置3个状态
# f[i][0]，i天结束的时候持有一只股票
# f[i][1], i天结束的时候不持有股票，处于冷冻期
# f[i][2], i天结束的时候持有股票，不处于冷冻期
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, len(prices)):
            new_f0 = max(f0, f2 - prices[i])  # 持有股票，当天不买，或者处于f2买股票
            new_f1 = f0 + prices[i]  # 不持有股票，处于冷冻期，当天卖了股票
            new_f2 = max(f1, f2)  # 不持有股票，不处于冷冻期，说明当天没有操作，前一天处于不持有股票的状态
            f0, f1, f2 = new_f0, new_f1, new_f2
        return max(f1, f2)
