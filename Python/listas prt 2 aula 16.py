'''
Listas prt2

'''
ListaMinMax = [5, 10, 20, 100, 50]

print(min(ListaMinMax)) # mostra o valor minino da lista 
print(max(ListaMinMax)) # mostra o valor maximo da lista 

print("\n-------------------------------------------------")

ListaNumeros1ate10 = [posicao for posicao in range(11)]
print(ListaNumeros1ate10)

print("\n-------------------------------------------------")

ListaDoisEmDois = list(range(0,10,2))
print(ListaDoisEmDois)

print("\n-------------------------------------------------")

ListaOriginal = ["Carro","Moto","Lancha","Avião"]
ListaCopiada = ListaOriginal.copy() # copia uma lista 

print(ListaCopiada)

print("\n-------------------------------------------------")

listaLetras = ["a","b","c"]
ListaNumeros = [1, 2, 3]
ListaCopiada2 = listaLetras + ListaNumeros

print(ListaCopiada2) # unindo as listas 

print("\n-------------------------------------------------")

listaLetras3 = ["a","b","c"]
ListaNumeros3 = [11, 22, 33]

for item in ListaNumeros3:
    listaLetras3.append(item) # imprime no final
    
print(listaLetras3)    

