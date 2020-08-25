A = [10,22,9,33,21,50,41,60]
n = len(A)

LIS = [1]*n

for i in range(1,n):
    for j in range(0,i):
        if A[i]>A[j] and LIS[i]<LIS[j]+1 :
            LIS[i] = LIS[j]+1
maximum = 0

for i in range(n):
    maximum = max(maximum, LIS[i])

print(maximum)