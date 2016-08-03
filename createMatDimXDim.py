def createMatDimXDim(dim):
    mat=[]
    subList=[]
    for i in range(dim):  #row
        for j in range(dim): #colum
            subList.append(i*10+j)
        mat.append(subList)
        subList=[]
    return mat

print (createMatDimXDim (4)) 
    
