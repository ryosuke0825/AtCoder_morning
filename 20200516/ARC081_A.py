import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)
max_1 = 0
max_2 = 0
for k, v in c.items():
    if v >= 2:
        if k > max_1:
            if v >= 4:
                max_1, max_2 = k, k
            else:
                max_1, max_2 = k, max_1
        elif k > max_2:
            max_2 = k

print(max_1*max_2)
