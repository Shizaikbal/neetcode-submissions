class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)

        dp[0] = 1
        for i in range(1, n+1):

            single_digit = int(s[i-1])
            if 1 <= single_digit <= 9:
                dp[i] = dp[i] + dp[i-1]

            if i >= 2:
                double_digit = int(s[i-2:i])
                if 10 <= double_digit <= 26:
                    dp[i] = dp[i] + dp[i-2]

        return dp[-1]
        