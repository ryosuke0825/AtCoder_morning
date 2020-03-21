n, l = map(int, input().split())

S = []
for _ in range(n):
    s = input()
    S.append(s)

S.sort()
print(''.join(S))
