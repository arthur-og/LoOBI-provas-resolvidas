import sys
input = sys.stdin.readline

M, N = map(int, input().split())
estoque = [[0]*N for _ in range(M)]
pecas_vendidas = 0

for i in range(M):
    linha = list(map(int, input().split()))
    for j in range(N):
        estoque[i][j] = linha[j]

P = int(input())
for _ in range(P):
    I, J = map(int, input().split())
    if (estoque[I-1][J-1] > 0):
        estoque[I-1][J-1]-=1
        pecas_vendidas+=1

print(f"Numero de pecas vendidas: {pecas_vendidas}")
