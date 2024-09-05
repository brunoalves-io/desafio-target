# Aqui, solicito um número ao usuário
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Aqui, eu inicializo os primeiros números da sequência de Fibonacci...
a = 0
b = 1

# Essa é a lista para armazenar a sequência de Fibonacci =)
fib_sequencia = [a, b]

while True:
    fib_prox = a + b
    if fib_prox > numero: # Aqui vai gerar a sequência de Fibonacci até o número informado pelo usuário
        break
    fib_sequencia.append(fib_prox)
    a, b = b, fib_prox

# Nessa parte, o programa verifica se o número pertence à sequência e printa para o usuário a resposta!
if numero in fib_sequencia:
    print(f"O número {numero} pertence à sequência de Fibonacci")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci")
