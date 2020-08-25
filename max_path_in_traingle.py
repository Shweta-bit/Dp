N = 4
tri = [[8,0,0,0],
       [-4,4,0,0],
       [2,2,6,0],
       [1,1,1,1]]

m = len(tri)-1
n = len(tri)-1
print(m)
print(n)

for i in range(m-1,-1,-1):
    for j in range(i+1):

        if (tri[i+1][j]>tri[i+1][j+1]):
            tri[i][j] += tri[i+1][j]
        else:
            tri[i][j] += tri[i+1][j+1]
print(tri[0][0])