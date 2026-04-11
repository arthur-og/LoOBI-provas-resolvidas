import sys
input = sys.stdin.readline

V = int(input())
A = int(input())
F = int(input())
P = int(input())
total = 0

contas = [A, F, P]
contas.sort()

for conta in contas:
    if V >= conta:
        V-=conta
        total+=1

print(f"Total de contas: {total}")
