import sys
input = sys.stdin.readline

N = int(input())
pessoas = {}
MIN = 1

for _ in range(N):
    nome = input().strip()
    lance = int(input())
    pessoas[nome] = lance

lance_max = MIN
# ganhador = next(iter(pessoas))
ganhador = ""

for pessoa, lance in pessoas.items():
    if lance > lance_max:
        lance_max = lance
        ganhador = pessoa

print(f"Ganhador: {ganhador} com um lance de {lance_max}")

