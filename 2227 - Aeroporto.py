#5% Presentation Error
contador = 1
aeroportos = []
while True:
    a, v = map(int, input().split())
    if a == v == 0:
        break

    grau = [0] * (a + 1)

    for _ in range(v):
        x, y = map(int, input().split())
        grau[x] += 1
        grau[y] += 1

    maior = max(grau[1:])
    resposta = [str(i) for i in range(1, a + 1) if grau[i] == maior]
    aeroportos.append(resposta[:])

for i in range(len(aeroportos)):
    print(f"Teste {contador}")
    print(" ".join(aeroportos[i]))
    print()
    contador += 1
