# n = 3
# dp = [0]*(n)
#
# dp[0] = 1
# dp[1] = 1
# for i in range(2,n):
#     dp[i] = dp[i-1]+dp[i-2]
# print(dp)

class Solution:
    def climbStairs(self, n):
        dp = [None]*(n)
        dp[0] = 1
        dp[1] = 1
        print(dp)
        for i in range(2,n):
            dp[i ] = dp[i-1]+dp[i-2]
        return len(dp)

g = Solution()
n = 2
print(g.climbStairs(n))