def addValuesInAllRows(mat):
    Sum=[]
    for i in range(len(mat)):
        colSum=0
        for j in range(len(mat)):
            colSum+=mat[i][j]
        Sum.append(colSum)
    return Sum

mat = [ [1,2,3], [10,20,30], [100,200,300] ]
list_sum_rows = addValuesInAllRows(mat) 
print(list_sum_rows)
