# 5% de erro
v, n = map(int, input().split())
t = n*v
for i in range(10, 100, 10):
    r = t*i/100
    if i == (v-1):
        if r == (r//1) or r-(r//1) >= 0.49:
            print(f"{round(r)}", end="...")
            print()
        else:
            print(f"{round(t*i/100)+1}", end="...")
            print()
    else:
        if r == (r // 1) or r - (r // 1) >= 0.5:
            print(f"{round(r)}", end=" ")
        else:
            print(f"{round(t * i / 100) + 1}", end=" ")
