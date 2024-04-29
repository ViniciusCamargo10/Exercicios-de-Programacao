linha = 0 

while linha < 3: 
    coluna = 0
    while coluna < 3:
        print("Linha: ", linha, "- Coluna", coluna)
        coluna += 1
    linha += 1 

#----------------------------------------------------------
print("\n")

numeroI = 1 

numeroF = int(input("Digite um numero maior que 1:"))

while numeroI <= numeroF:
    print(numeroI)
    numeroI += 1 
    
#-------------------------

print("\n")

numero = 1
numeroPar = int(input("Digite um número maior que 1: "))

while numero <= numeroPar:
    #Verifica se o número é PAR
    if numero % 2 == 0:
        print(numero, end=" ")
    numero += 1

