listaNomes = ["Danielle","Vinicius","Rabi"]

for posicao in listaNomes:
    if posicao == "Vinicius":
        continue 
    print(posicao)

#continue usa para pular o que foi pedido     
    
print("\n-------------------------------------")

for i in range(11):
    print(i)

#range usa para contar 

print("\n-------------------------------------")

#range usa para contar por exemplo a partir do 1 
#para parar no 11 por exemplo 
#e step para contar de 2 em dois ou em outros...
#sempre na ordem start , stop, step
print("\n-------------------------------------")

for Posicao in range(1, 11, 1):
    print(Posicao)
    
print("\n-------------------------------------")

for Posicao in range(20, 9, -1):
    print(Posicao)
