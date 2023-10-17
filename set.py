#set ordena a ordem por si proprio
#set não permite duplicidade


conjuto1 = set([1,2,3,4,5,6,7])

conjuto2 = set([5,6,7,8,9,10,11])

uniaoo = conjuto1 | conjuto2
print(uniaoo) ## uniao
##
#print(conjuto1.intersection(conjuto2))
print(conjuto1 & conjuto2)

print(conjuto1 - conjuto2) #diferença 
print(conjuto2 - conjuto1)

print( conjuto1 ^ conjuto2) #diferença simetrica

lista = [1,2,3,4,5,6,7,8,4,3,2,2,7,8,0,1,2,4,5]
print(lista)

lista_set = set(lista)
print(lista_set)

print(8 in lista_set)