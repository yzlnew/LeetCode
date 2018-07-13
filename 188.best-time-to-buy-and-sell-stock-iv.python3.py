class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if not prices or not k:
            return 0

        if k >= len(prices) / 2:
            profit = 0

            for i in range(len(prices) - 1):
                profit += max(0, prices[i + 1] - prices[i])

            return profit

        sell = [0] * (k + 1)
        buy = [-2**31] * (k + 1)

        for i in range(len(prices)):
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - prices[i])
                sell[j] = max(sell[j], buy[j] + prices[i])

        return sell[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit(2, [3, 2, 6, 5, 0, 3]))
