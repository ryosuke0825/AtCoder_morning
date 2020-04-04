N, M = map(int, input().split())

SC = []
for _ in range(M):
    s, c = map(int, input().split())
    SC.append([s, c])

for i in range(1000):
    str_i = str(i)
    if len(str_i) != N:
        continue

    for sc in SC:
        index = sc[0]-1

        if len(str_i) != N:
            break
        if str_i[index] != str(sc[1]):
            break
    else:
        print(i)
        exit(0)
print(-1)
