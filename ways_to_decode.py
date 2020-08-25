s = "12"
n = len(s)
dp = [None]*(n+1) #going to store number of ways to decode
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    dp[i] = 0
    if s[i-1] > '0':
        dp[i] = dp[i-1]
    if (s[i-2]=='1'or (s[i-2]=='2' and s[i-1]<'7')):
        dp[i] += dp[i-2]
print(dp)

