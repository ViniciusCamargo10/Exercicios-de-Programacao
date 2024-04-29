"""
+ = soma
- = subritação
* = multiplicação 
/ = divisão 
// = divisao mas mostra só o primeiro numero  
% = retorna o resto da divisao 
** = potencia 
"""

numero1 = 10 
numero2 = 3

soma = numero1 + numero2 
 
print(f"A soma de {numero1} e de {numero2} é igual a: {soma}")

menos = numero1 - numero2 
print("Subtração:", menos)

vezes = numero1 * numero2 
print("multiplicação:", vezes)
print(numero1 * "D")

divisao = numero1 / numero2 
print(f"A divisao de {numero1} e de {numero2} é igual a: {divisao}")

divisao2 = numero1 // numero2 
print(f"A divisao de {numero1} e de {numero2} é igual a: {divisao2}")

modulo = numero1 % numero2
print(f"O resto da divisão de {numero1} e {numero2} é: {modulo}")

potencia = numero1 ** numero2
print("Numero1 elevado: ", potencia)

