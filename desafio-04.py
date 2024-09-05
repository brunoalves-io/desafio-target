# a) 1, 3, 5, 7, ___
seq_a = [1, 3, 5, 7]
prox_a = seq_a[-1] + 2 # Aqui pego o último número da lista e somo com 2

# b) 2, 4, 8, 16, 32, 64, ____
seq_b = [2, 4, 8, 16, 32, 64]
prox_b = seq_b[-1] * 2 # Aqui pego o último número da lista e multiplico por 2

# c) 0, 1, 4, 9, 16, 25, 36, ____
seq_c = [0, 1, 4, 9, 16, 25, 36]
prox_c = (len(seq_c)) ** 2 # Aqui uso exponenciação, a lista se trata de quadrados de números naturais e o próximo será 7²

# d) 4, 16, 36, 64, ____
seq_d = [4, 16, 36, 64]
prox_d = (len(seq_d) + 6) ** 2 # Quadrados de números pares

# e) 1, 1, 2, 3, 5, 8, ____ 
seq_e = [1, 1, 2, 3, 5, 8]
prox_e = seq_e[-1] + seq_e[-2] # Aqui pego o último número e o penúltimo número e somo os dois para gerar o próximo

# f) 2, 10, 12, 16, 17, 18, 19, ____
seq_f = [2, 10, 12, 16, 17, 18, 19]
prox_f = seq_f[-1] + 1 # Começa com uma sequência misturada e nos 4 últimos inicia o padrão, então pego o último número e somo com 1

print(prox_a, prox_b, prox_c, prox_d, prox_e, prox_f)
