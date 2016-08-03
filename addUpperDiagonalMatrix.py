def addUpperDiagonalMatrix (mat):
    sum=0
    for i in range(len(mat)):
        for j in range(i,len(mat)):
            sum+=mat[i][j]
    return sum
val = addUpperDiagonalMatrix ([[1,2,3,4],[10,20,30,40],[100,200,300,400],[1000,2000,3000,4000]])
print (val)
