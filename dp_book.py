# n = int(input("number: "))

# sun of n positive integrs
# sum  = 0
# # for i in range(n>=0):
# #     if n==0:
# #         print(sum)
# #     else:
# #         add=n*(n+1)/2
# #     print(add)
# #
#
# for i in range(1,n+1):
#     sum+= i
# print(sum)

#factorial
# fact =1
#
#
# for i in range(1,n+1):
#     fact = i*fact
# print(fact)
# def recur_function(n):
#     if n==1:
#         return 1
#     else:
#         return n*recur_function(n-1)
# n = 4
# if n < 0:
#     print('no fact')
# elif n==0:
#     print('1')
# else:
#     print(recur_function(n))

# A = [1,2,3,4,5,6]
# n = len(A)
#
# for i in range(1,n):
#     A[i] += A[i-1]
#
# print(A)

# Python program for implementation of Bubble Sort
# arr = [64, 34, 25, 12, 22, 11, 90]
# n = len(arr)
# for i in range(n-1):
#         # range(n) also work but outer loop will repeat one time more than needed.
#
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
#
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#             # Driver code to test above
#
#
#
# print ("Sorted array is:")
# for i in range(len(arr)):
#     print ("%d" %arr[i]),
table = []
n = 4
for i in range(1,11):
    table.append(n*i)
print(table)