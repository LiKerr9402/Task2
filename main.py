try:
    n = int(input())
except ValueError:
    print("Ошибка!")
    exit(0)
if (n == 0):
    print("Введенный ранг матрицы равен нулю!")
    exit(0)
res = [[0] * n for i in range(n)]
count, m = 1, 0
res[n // 2][n // 2] = n * n
for v in range(n // 2):
    for i in range(n - m):
        res[v][i + v] = count
        count += 1
    for i in range(v + 1, n - v):
        res[i][-v - 1] = count
        count += 1
    for i in range(v + 1, n - v):
        res[-v - 1][-i - 1] = count
        count += 1
    for i in range(v + 1, n - (v + 1)):
        res[-i - 1][v] = count
        count += 1
    m += 2
for i in res:
    print(*i)
