numeroInteiro = int(input("Digite um número inteiro entre 1 e 100: "))
print(f"O número digitado foi: {numeroInteiro}")

if 90 <= numeroInteiro <= 100:
    print("Sua classificação é A. Parabéns!")
elif 80 <= numeroInteiro < 90:
    print("Sua classificação é B. Muito Bom!")
elif 70 <= numeroInteiro < 80:
    print("Sua classificação é C. Bom trabalho!")
elif 60 <= numeroInteiro < 70:
    print("Sua classificação é D. Precisa melhorar!")
elif numeroInteiro < 60:
    print("Sua classificação é F. Estude mais!")
else:
    print("O número digitado é inválido.")
