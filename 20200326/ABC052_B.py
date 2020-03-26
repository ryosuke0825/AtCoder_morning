n = int(input())
S = input()

x = 0
ans = x
for s in S:
    if s == 'I':
        x += 1
    else:
        x -= 1
    ans = max(ans, x)
print(ans)
