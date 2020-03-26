n = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

ans = 0
for i in range(n):
    tmp = sum(A1[:i+1])
    tmp += sum(A2[i:])
    ans = max(ans, tmp)
print(ans)
