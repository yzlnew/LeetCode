class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_cur = max_so_far = 0
        for i in range(1,len(prices)):
            max_cur += prices[i] - prices[i-1]
            max_cur = max(0, max_cur)
            max_so_far = max(max_cur, max_so_far)

        return max_so_far
