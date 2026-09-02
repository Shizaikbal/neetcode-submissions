class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]

        start = 0
        max_len = 1

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                
                length = j-i+1

                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True

                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length

        return s[start:start+max_len]



        