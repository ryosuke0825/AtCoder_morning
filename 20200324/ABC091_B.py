n = int(input())
S = {}
for _ in range(n):
    s = input()
    if s in S:
        S[s] += 1
    else:
        S[s] = 1

m = int(input())
T = {}
for _ in range(m):
    t = input()
    if t in T:
        T[t] += 1
    else:
        T[t] = 1

ans = 0
for k in S.keys():
    if k in T:
        ans = max(ans, S[k]-T[k])
    else:
        ans = max(ans, S[k])
print(ans)
