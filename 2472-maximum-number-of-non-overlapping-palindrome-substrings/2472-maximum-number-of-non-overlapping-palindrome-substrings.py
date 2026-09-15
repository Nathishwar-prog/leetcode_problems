class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome DP
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if length == 1:
                    pal[i][j] = True

                elif length == 2:
                    pal[i][j] = s[i] == s[j]

                else:
                    pal[i][j] = s[i] == s[j] and pal[i + 1][j - 1]

        # dp[i] = maximum number of valid palindromes
        # that can be selected from s[0:i]
        dp = [0] * (n + 1)

        for j in range(n):
            # Don't select a palindrome ending at j
            dp[j + 1] = dp[j]

            # Try every substring ending at j
            for i in range(j + 1):
                length = j - i + 1

                if length >= k and pal[i][j]:
                    dp[j + 1] = max(dp[j + 1], dp[i] + 1)

        return dp[n]
            