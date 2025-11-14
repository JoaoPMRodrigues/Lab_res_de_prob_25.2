n = int(input())
frases = []
for i in range(n):
    frases.append(list(map(str, input().split())))
for palavra in range(len(frases)):
    for letra in range(len(frases[palavra])):
        print(frases[palavra][letra][0], end="")
    print()
