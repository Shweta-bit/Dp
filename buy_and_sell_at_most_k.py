# # def stocks(A, k):
# A = [3, 2, 6, 5, 0, 3]
# k = 2
# n = len(A)
# profit = [[None for x in range(n)] for y in range(k+1)]
#
# for i in range(k+1):
#     for j in range(n):
#
#         if i==0 or j==0:
#             profit[i][j] = 0
#         else:
#             max_so_far = 0
#             for x in range(j):
#                 curr_price = A[j] - A[x] + profit[i-1][x]
#                 if max_so_far < curr_price:
#                     max_so_far = curr_price
#
#             profit[i][j] = max(profit[i][j-1], max_so_far)
# print(profit[k][n-1])


# Find maximum profit earned from at most k stock transactions
# Input to the function are stock prices of n days and positive number k
price = [10,6,8,4,2]
k = 2
    # get number of days n
n = len(price)

    # profit[i][j] stores the maximum profit gained by doing
    # at most i transactions till j'th day
profit = [[None for x in range(n + 1)] for y in range(k + 1)]

    # fill profit matrix in bottom-up fashion
for i in range(k + 1):

        # initialize prev diff to minus infinity
    prev_diff = float('-inf')

    for j in range(n):

            # profit is 0 when:
            # i = 0 i.e. for 0'th day
            # j = 0 i.e. no transaction is being performed
        if i == 0 or j == 0:
            profit[i][j] = 0
        else:
            prev_diff = max(prev_diff, profit[i - 1][j - 1] - price[j - 1])
            profit[i][j] = max(profit[i][j - 1], price[j] + prev_diff)

print(profit[k][n - 1])



