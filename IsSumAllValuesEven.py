def isSumAllValuesEven(mat):
    sum=0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            sum+=mat[i][j]
    print sum
    if sum%2==0:
        return True
    else:
        return False
    
mat=[[1,1,1],[2,2,2]]
res = isSumAllValuesEven(mat)
print (res) 

