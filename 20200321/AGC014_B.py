n, m = map(int, input().split())

ans = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    ans[a-1] += 1
    ans[b-1] += 1

for a in ans:
    if a % 2 != 0:
        print('NO')
        break
else:
    print('YES')