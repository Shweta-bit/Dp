# def stocks(A):
#     n = len(A)
#     buy = 0
#     max = 0
#     for i in A:
#         buy = min(A)
#         sale = max(A)




A = [7,1,5,3,6,4]
n = len(A)
if n==0:
    print(0)
sol = 0
min_p=A[0]
for i in range(n):
    if (A[i]<min_p):
        min_p = A[i]
    sol = max(sol, A[i]-min_p)
print(sol)
# buy_day = 0
# for i in range(n):
#     buy = min(A)
#     buy_day
# buy = min(A)
# sale = max()
# print(buy)
# print(sale)
# max_profit = sale - buy
# print(max_profit)