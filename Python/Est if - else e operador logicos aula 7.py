'''
--------------------------
estrutura if 

if alguma variavel : 
    print("")
else:
    print(")

-----------------------

Operador and (E)
Operador or (ou)
Operador not (nao)

'''
# operador and
n1 = 21 
n2 = 10
n3 = 40

if n1 > n2 and n3 > n1:
    print("ambas condições estão corretas")
    
nome = "Vinicius"
idade = 16 

#estrutura if else

if nome == "Vinicius" and idade >= 17:
    print("As informações são verdadeiras")
else:
    print("As informações sao falsas")

#operador or     
numero1 = 10 
numero2 = 5 
numero3 = 15

if numero1 > numero2 or numero1 > 5:
    print("pelo menos uma das condições é verdadeira")

#operador not 

nt = 0

if not nt:
    print("o numero nao pode ser zero")
