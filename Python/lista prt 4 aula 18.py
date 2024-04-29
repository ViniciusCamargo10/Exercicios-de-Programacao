listaNomes = ["Vi","gi", "DAni","GU"]
for i in listaNomes:
    print(i)
    
print("\n")

#para fazer um loop precisa definir o inicio 
i = 0 
while i < len(listaNomes): # len converte para numero 
    print(listaNomes[i])
    i = i + 1 
    
print("\n")

listaNomesI = []
for item in listaNomes:
    if "i" in item:
        listaNomesI.append(item)
print(listaNomesI)
print("\n")
ListaMaiscula = [item.upper() for item in listaNomes ]
ListaMinuscula = [item.lower() for item in listaNomes]
print(listaNomes)
print(ListaMinuscula)
print(ListaMaiscula)
