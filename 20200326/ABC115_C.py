n, k = map(int, input().split())

tree = []
for _ in range(n):
    tree.append(int(input()))

tree.sort()
ans = 10**9
for i in range(n-k+1):
    ans = min(ans, tree[i+k-1]-tree[i])
print(ans)
