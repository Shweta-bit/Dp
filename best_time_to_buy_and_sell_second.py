def stocks(A):
    max_profit = 0
    n = len(A)
    if (n)<=1 :
        return max_profit
    for i in range(1,n):
        if A[i]>A[i-1]:
            max_profit += A[i] - A[i-1]
    return max_profit

A = [7,6,4,3,1]
print(stocks(A))
