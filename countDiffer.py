def countDiffer(st):
    Ucount=0
    Lcount=0
    for i in st:
        if i.isupper():
            Ucount+=1
        if i.islower():
            Lcount+=1
    return Lcount-Ucount
st="Hello"
result=countDiffer(st)
print(result)
        
