from typing import List
# dp 分买或者卖 各有k个状态
# dp[奇数索引]表示第i次买入总的收益
# dp[偶数索引]表示第i次卖出总的收益

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0] * (2 * k + 1)
        dp[1] = -prices[0] #对于第一天的价格，只有第一次买入
        for i in range(3, len(dp), 2):
            dp[i] = float("-inf") #初始化，对于第i次买入，由于每次买入收益是负值，初始化要为负无穷
        for i in range(1, len(prices)):
            dp[1] = max(dp[1], -prices[i]) # 第一次买入
            dp[2] = max(dp[2], dp[1] + prices[i]) # 第一次卖出
            for j in range(2, min(i, k) + 1):
                dp[2 * j - 1] = max(dp[2 * j - 1], dp[2 * j - 2] - prices[i]) #第j次买入
                dp[2 * j] = max(dp[2 * j], dp[2 * j - 1] + prices[i]) #第j次卖出
        max_profit = 0
        for i in range(2, min(len(prices) + 1, len(dp)), 2):
            if max_profit < dp[i]:
                max_profit = dp[i] # 求出卖出的时候最大收益
        return max_profit


print(Solution().maxProfit(4, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))
