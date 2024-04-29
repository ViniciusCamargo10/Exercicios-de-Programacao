numero1 = 10 
numero2 = 10 

if numero1 > numero2: 
    print(f"A condição que diz que {numero1} é maior que {numero2}")
elif numero1 == numero2:
    print(f"A condição diz que {numero1} é igual a {numero2} portanto os numeros sao iguais ")
else:
    print("nenhuma condição foi atendida")
    
#-------------------------------------------------

# outra forma de escrever if 

num1 = 50
num2 = 12

print("num1 é maior") if num1 > num2 else print("num 2 é maior")
