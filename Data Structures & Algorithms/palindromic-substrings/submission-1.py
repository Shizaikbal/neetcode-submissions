class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for i in range(n)]

        count = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                length = j-i+1

                if length == 1:
                    dp[i][j] = True
                    count += 1
                elif length == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        count += 1
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        count += 1

        return count
        