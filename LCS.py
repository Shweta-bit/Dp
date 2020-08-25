

A = "abbcdgf"
B = "bbadcgf"
m = len(B)
n = len(A)

L = [[None]*(m+1) for i in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i==0 or j==0:
            L[i][j] =0
        elif A[i-1]==B[j-1]:
            L[i][j] = L[i-1][j-1]+1
        else:
            L[i][j] = max(L[i-1][j], L[i][j-1])
print(L[n][m])






