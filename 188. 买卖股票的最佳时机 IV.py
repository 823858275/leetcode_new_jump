from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0] * (2 * k + 1)
        dp[1] = -prices[0]
        for i in range(3, len(dp), 2):
            dp[i] = float("-inf")
        for i in range(1, len(prices)):
            dp[1] = max(dp[1], -prices[i])
            dp[2] = max(dp[2], dp[1] + prices[i])
            for j in range(2, min(i, k) + 1):
                dp[2 * j - 1] = max(dp[2 * j - 1], dp[2 * j - 2] - prices[i])
                dp[2 * j] = max(dp[2 * j], dp[2 * j - 1] + prices[i])
        max_profit = 0
        for i in range(2, min(len(prices) + 1, len(dp)), 2):
            if max_profit < dp[i]:
                max_profit = dp[i]
        return max_profit


print(Solution().maxProfit(4, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))
