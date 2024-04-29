"""
Listas em python

"""
listasNomes = ["Vinicius","Gi","Dani"]
print(len(listasNomes)) # len apresenta o tamanho da lista 

print("\n")

lista1 = ["a","b","c"]
lista2 = [1, 2, 3, 4]
lista3 = [True, False, False]
lista4 = ["Roberta", 34, False]

print(lista1)
print(lista2)
print(lista3)
print(lista4)

#apenas pra mostrar que aceita os tipos misturados

#---------------------------------
print("\n")

#                0   1   2      3 
listaPosicao = ["a","b","c","Elefante"]
print(listaPosicao[2])

print("\n")
print(listaPosicao[-1]) #Ultimo item da lista, com o - pega de tras para frente 

print("\n")
print(listaPosicao[1:3])# imprime os especificos 

print("\n")
print(listaPosicao[:3]) # imprime até o terceiro item 

print("\n")
print(listaPosicao[2:]) # imprime a partir do terceiro item 

print("\n")
print(listaPosicao[::2]) # imprime de dois em dois 

print("\n")
print(listaPosicao[::-1]) # imprime a lista de tras para frente

