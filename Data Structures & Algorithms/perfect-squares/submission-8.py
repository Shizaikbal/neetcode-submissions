class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        squares= []
        i=1
        while i*i <= n:
            squares.append(i*i)
            i += 1


        for i in range(1, n+1):
            for square in squares:
                if square <= i:
                    dp[i] = min(dp[i], 1 + dp[i-square])
                else:
                    break

        return dp[-1] if dp[-1] != float('inf') else -1