n = int(input())

ans = 0
for i in range(111, 1000):
    str_i = str(i)
    if str_i.count('0') != 0:
        continue

    for j in range(n+1, 10):
        if str_i.count(str(j)) != 0:
            break
    else:
        ans += 1

print(ans)
