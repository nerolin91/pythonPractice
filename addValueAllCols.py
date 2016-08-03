def addValuesInAllCols (mat):
    colSum=[]
    sum=0
    for i in range (len(mat)):
        for j in range (len(mat)):
            sum+=mat[j][i]
        colSum.append(sum) 
        sum=0
    return colSum

mat = [ [1,2,3], [10,20,30], [100,200,300] ]
list_sums_cols = addValuesInAllCols(mat)
print (list_sums_cols)
            
        

