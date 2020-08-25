A = 'bebeeed'

import itertools
lib = []
combs = []
ans = []
for l in range(1, len(A)+1):
    combs.append(list(itertools.combinations(A, l)))
for c in combs:
    for t in c:
        lib.append(len(t))
        ans.append(''.join(t))

checker = []
for x in ans:
    if x.upper() == x[::-1].upper():
        checker.append(len(x))


print(max(checker))


n = len(A)
L = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
    L[i][i] = 1

for cl in range(2, n+1):
    for i in range(n-cl+1):
        j = i+cl-1
        if A[i] == A[j] and cl == 2:
            L[i][j] = 2
        elif A[i] == A[j]:
            L[i][j] = L[i+1][j-1]+2
        else:
            L[i][j] =max(L[i][j-1], L[i+1][j])

print(L[0][n-1])

# // O(N^2 log(N)) solution first, then O(N^2) below
# bool is_palindrome(string s) {
#     string rev = s;
# reverse(rev.begin(), rev.end());
# return s == rev;
# }
# // returns true if there is a palindrome of length x
# int good(int x, string s) {
# int n = s.length();
# for(int L = 0; L + x <= n; L++) {
# if(is_palindrome(s.substr(L, x))) {
# return L;
# }
# }
# return -1;
# }
# class Solution {
# public:
#     string longestPalindrome(string s) {
#     int best_len = 0;
# string best_s = "";
# int n = s.length();
# for(int parity : {0, 1}) {
#     int low = 1, high = n;
# if(low % 2 != parity) low++;
# if(high % 2 != parity) high--;
# while(low <= high) {
# int mid = (low + high) / 2;
# if(mid % 2 != parity) {
# mid++;
# }
# if(mid > high) {
# break;
# }
# int tmp = good(mid, s);
# if(tmp != -1) {
# if(mid > best_len) {
# best_len = mid;
# best_s = s.substr(tmp, mid);
# }
# low = mid + 2;
# }
# else {
# high = mid - 2;
# }
# }
# }
# return best_s;
# }
# };
#
# // ===================
#
# class Solution {
# public:
#     string longestPalindrome(string s) {
#     int best_len = 0;
# string best_s = "";
# int n = s.length();
# for(int mid = 0; mid < n; mid++) {
# for(int x = 0; mid - x >= 0 && mid + x < n; x++) {
# if(s[mid-x] != s[mid+x]) {
# break;
# }
# int len = 2 * x + 1;
# if(len > best_len) {
# best_len = len;
# best_s = s.substr(mid - x, len);
# }
# }
# }
# for(int mid = 0; mid < n - 1; mid++) {
# for(int x = 1; mid - x + 1 >= 0 && mid + x < n; x++) {
# if(s[mid-x+1] != s[mid+x]) {
# break;
# }
# int len = 2 * x;
# if(len > best_len) {
# best_len = len;
# best_s = s.substr(mid - x + 1, len);
# }
# }
# }
# return best_s;
# }
# };