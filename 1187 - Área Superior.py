matriz = list()
auxiliar = list()
operacao = str(input().upper())

for i in range(12):
    for j in range(12):
        auxiliar.append(float(input()))
    matriz.append(auxiliar[:])
    auxiliar.clear()
total = 0
inicio = 1
fim = 11

soma = 0
for i in range(5):
    for j in range(inicio, fim):
        soma += matriz[i][j]
        total += 1
    inicio += 1
    fim -= 1

if operacao == "S":
    print(f"{soma:.1f}")
else:
    media = soma/total
    print(f"{media:.1f}")
