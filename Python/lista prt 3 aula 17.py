lista1 = [1,2,3]
lista2 = ["a", "b", "c"]

lista1.extend(lista2) #une as listas 
print(lista1)

print("\n")

lista1.remove("c") #remove o que foi pedido
print(lista1)

print("\n")

lista1.pop(2) #remove o segundo eletemento da lista nesse caso 
print(lista1)

print("\n")

lista1.pop() #remove o ultimo eletemento
print(lista1)

print("\n")

del lista1 [0] # remove o primeiro eletemento da lista 
print(lista1)

print("\n")

#lista1.clear()  remove tudo 
#print(lista1)

print("\n")

lista1.append("queijo") # add na lista 
print(lista1)

lista1.insert(1,"pastel")
print(lista1)

print("\n")

if "pastel" in lista1:  #verificando se está na lista 
    print("Sim está na lista")
else:
    print("Não encontramos na lista")

print("\n")

lista1[2] = ("banana")

print(lista1)

lista1[1:4] = ["A","B"] 

print(lista1)

