"""
A diferença das listas para as tuplas  é que 
não podemos editar os elementos, adicionar e remover

"""
tuplaLetras = ("a", "b", "c") # a diferença de uma tupla pra list é que lista é [] e tupla ()
print(tuplaLetras)
print(type(tuplaLetras))
print(len(tuplaLetras))
print(tuplaLetras[0])
print(tuplaLetras[-1])

print("\n")

novaTupla = ("d",) # para ser reconhecido como tupla precisa colocar ("alguma coisa" ,)
print(novaTupla)
print(type(novaTupla))
tuplaLetras += novaTupla #une duas tuplas 
print(tuplaLetras)

print("\n")

tuplaNumeros = (1, 2, 3, 4, 5, 6,)
listaNumeros = list(tuplaNumeros) # converte para lista para poder remover 
listaNumeros.remove(5)
tuplaNumeros = tuple(listaNumeros)
print(tuplaNumeros)

for item in tuplaNumeros:
    print(item)
