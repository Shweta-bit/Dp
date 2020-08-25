class Solution:
    def minDistance(self, A, B):

        m = len(A)
        n = len(B)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    dp[i][j] =j
                elif j==0:
                    dp[i][j] = i
                else:
                    if A[i-1] == B[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1+min(min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1])

        return dp[m][n]

A = 'HORSE'
B = 'ROS'
g = Solution()
print(g.minDistance(A,B))