N = int(input())
H = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    while True:
        if H[i] == 0:
            break

        for j in range(i+1, N):
            if H[j] == 0:
                break

            H[j] -= 1
        H[i] -= 1
        ans += 1
ans += max(0, H[-1])
print(ans)
