abc = list(map(int, input().split()))


ans = 0
while True:
    if abc[0] == abc[1] == abc[2]:
        print(ans)
        exit(0)

    if abc.count(max(abc)) >= 2:
        abc[abc.index(min(abc))] += 2
    else:
        if abc[0] != max(abc):
            abc[0] += 1
        if abc[1] != max(abc):
            abc[1] += 1
        if abc[2] != max(abc):
            abc[2] += 1
    ans += 1
