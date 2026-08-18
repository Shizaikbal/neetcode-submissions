class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) 
        dp = [-1] * n
        dp[-1] = cost[-1]
        for i in range(n-2, -1, -1):
            if i == n-2:
                dp[i] = min(cost[i]+dp[i+1], cost[i])
            else:
                dp[i] = min(cost[i]+dp[i+1], cost[i]+dp[i+2])

        result = min(dp[0], dp[1])
        return result