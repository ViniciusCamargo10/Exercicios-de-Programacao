dicionario = {
    "Dani": 18,
    "Gica": 15,
    "Vini": 18
    
}

print(dicionario)
print(len(dicionario))
print(type(dicionario))

print("\n")

dicionario2 = dicionario.copy() #copia o dicionario
print(dicionario2)

print("\n")

dicionario3 = dict(dicionario) # outra forma de copiar 
print(dicionario)

print("\n")

dados = dicionario["Dani"] # pega os dados
print(dados)

dados2 = dicionario.get("Gica") # pega os dados 
print(dados2)
print("\n")

nomes = dicionario.keys() # pega os nomes 
print(nomes)

print("\n")

idade = dicionario.values()
print(idade)
print("\n")

dicionarioAlimentos = {
    "arroz": 10.50,
    "carne": 25.50,
    "lasanha": 14,
    "uva": 8,
    "morango": 15
}

print(dicionarioAlimentos)

dicionarioAlimentos["lasanha"] = 37 

print(dicionarioAlimentos)

#OUTRA FORMA DE ALTERAR O PREÇO 

dicionarioAlimentos.update({"carne": 20 })
print(dicionarioAlimentos)

dicionarioAlimentos["Picanha"] = 58 # add 
print(dicionarioAlimentos)

dicionarioAlimentos.pop("carne") # remove 
print(dicionarioAlimentos)

dicionarioAlimentos.popitem() #remove o ultimo item do dicionario 
print(dicionarioAlimentos)
 
# dicionarioAlimentos.clear() # remove tudo de uma vez
# print(dicionarioAlimentos)

print("\n")

del dicionarioAlimentos["arroz"]
print(dicionarioAlimentos)
print("\n")

if "uva" in dicionarioAlimentos:
    print("A uva está no dicionario")
else:
    print("O item não foi encontrado")
print("\n")

DicionarioLetras = {
    "Letra 1": "A",
    "Letra 2": "B",
    "Letra 3": "C",
    "Letra 4": "D",
    "Letra 5": "E",
    "Letra 6": "F",
    "Letra 7": "G"
}

print(DicionarioLetras)

for posicao in DicionarioLetras: #imprime apena os titulos
    print(posicao)
    
for i in DicionarioLetras:
    print(DicionarioLetras[i]) #apenas os valores 

print("\n")

for valor in DicionarioLetras.values(): #apenas os valores exemplo 2 
    print(valor)
    
for titulo, valores in DicionarioLetras.items():
    print(titulo, "-", valores)
    
print("\n")

exemplo1 = {
    "A": 1,
    "B": 2
}    

exemplo2 = {
    "C": 3,
    "D": 4
}    

exemplo3 = {
    "E": 5,
    "F": 6
}        

unirVariosDicionarios = {
    "dicionario1": exemplo1,
    "dicionario2": exemplo2,
    "dicionario3": exemplo3
}

print(unirVariosDicionarios)


print("\n\n")

escola = {
    "Turma 1" : {
        "Andre:" : 10,
        "Amanda:" : 8
    },
    "Turma 2" : {
        "Cesar:" : 6,
        "Alessandra:" : 7
    },
    "Turma 3" : {
        "Roger:" : 9,
        "Rosiane:" : 10
    }
}

for tur1, tur2 in escola.items():
    print(tur1)
    for tur1, tur2 in tur2.items():
        print("Aluno:", tur1, "- Nota:", tur2)




