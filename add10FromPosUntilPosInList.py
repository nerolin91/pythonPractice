def add10FromPosUntilPosInList (lista,pos1,pos2):
    for i in range(pos1,pos2+1):
        lista[i]+=10
    return lista
lista = [0,100,200,300,400,500]
lista = add10FromPosUntilPosInList(lista, 1, 4)
print(lista) 
