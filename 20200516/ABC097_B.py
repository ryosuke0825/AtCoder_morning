X = int(input())

if X == 1:
    print(1)
    exit(0)

ans = 0
for i in range(1, X+1):
    for j in range(2, X+1):
        if i**j > X:
            break
        else:
            ans = max(ans, i**j)

print(ans)
