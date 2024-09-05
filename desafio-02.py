# Aqui, solicito um texto ao usuário
texto = str(input("Digite aqui alguma coisa: "))

# Inicializo contadores
contagem_a = 0

# Percorre cada caractere da string
for caractere in texto:
    # Aqui, o programa verifica se o caractere é 'a' ou 'A'
    if caractere == 'a' or caractere == 'A': # Também poderia usar texto.lower e coverter toda a string em letras minúsculas
        contagem_a += 1

# Nessa parte, o programa verifica se e quantas vezes a letra A aparece na string digitada pelo usuário
if contagem_a > 0:
    print(f"A letra 'a' (ou 'A') aparece {contagem_a} vezes na string.")
else:
    print("A letra 'a' (ou 'A') não aparece na string.")
