n, k = map(int, input().split())
P = list(map(int, input().split()))

me = [0]
for i in range(n):
    p = (P[i] * (P[i] + 1) / 2) / P[i]
    me.append(me[(i+1)-1]+p)

ans = 0
for i in range(k, n+1):
    ans = max(ans, me[i]-me[i-k])
print(ans)
