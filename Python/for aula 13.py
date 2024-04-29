listasletras = ["a","b","c","d","e"]

#for = para

for posicao in listasletras:
    print("Letra:",posicao)
    
print("\n------------------------------------")


for posicao, letras in enumerate(listasletras): # enumerate fala a posicao das coisas 
    print(posicao, letras)
    
print("\n------------------------------------")    

for i in "Python":
    print(i)
    
print("\n------------------------------------")   

listaCores = ["azul","verde","amarelo","roxo"]

for i in listaCores:
    if i == "azul":
        print("Azul foi encontrado com sucesso")
        break
    
