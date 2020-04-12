import collections

N = int(input())

A = []
for _ in range(N):
    a = input()
    A.append(a)

CA = collections.Counter(A)
ans = 0
for v in CA.values():
    ans += (v-1)
print(ans)
