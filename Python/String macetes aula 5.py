'''
len --> conta, ja que é em string no caso quantas letras
usa o str antes para converter 

[] 0 = V ; 1 = i pelo exemplo 

[1:8] pega das letras 1 a 8 

[0:] pega tudo 

'''

nome = "Vinicius Souza Camargo "

print(nome)
print("Total de caracteres: " + str(len(nome)))

print(nome[0])

print(nome[0:8])

print(nome[0:])
#------------------------------------------

#upper retorna todas as letras em maiuscula 

frase = "DaniELLe Ama Vinicius"

print(frase.upper())

#lower retorna todas as letras em maiuscula 

frase = "DaniELLe Ama Vinicius"

print(frase.lower())

#-------------------------------------------

#replace --> subistituir 

notaProva = "Tirei nota tres na prova"
print(notaProva.replace("tres","dez"))
#-------------------------------------------

cpf = "515.991.818-35"

#pega apenas os pontos
cptPartes = cpf.split(".")

print(cptPartes)

#-------------------------------------------

palavraComEspaço = "        CURSO DE PYTHON         "
print(palavraComEspaço)
print(palavraComEspaço.strip()) #remove o Espaço

#-------------------------------------------

Frutas = "Gosto de uva"
print("maça" in Frutas)

res= Frutas.find("u")
print(res)

#-------------------------------------------

# .2f para duas casas apenas 

