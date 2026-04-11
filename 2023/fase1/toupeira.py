# Dados o mapa de túneis e salões de convivência, e uma lista de sugestões de passeio, escreva um
# programa que determine quantas sugestões de passeio são possíveis.

import sys
input = sys.stdin.readline

S, T = map(int, input().split())
passeios_possiveis = 0
adj = [[0] * S for _ in range(S)]

for _ in range(T):
    x, y = map(int, input().split())

    adj[x-1][y-1] = 1
    adj[y-1][x-1] = 1

P = int(input())
for _ in range(P):
    dados = list(map(int, input().split()))
    N = dados[0]
    passeio = dados[1:]
    valido = True

    for i in range(len(passeio) - 1):
        primeiro = passeio[i] - 1
        segundo = passeio[i + 1] - 1

        if adj[primeiro][segundo] == 0:
            valido = False
            break

    if valido:
        passeios_possiveis+=1

print(f"Numero de passeios possiveis: {passeios_possiveis}")
