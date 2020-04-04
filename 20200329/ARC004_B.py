n = int(input())
D = []
for _ in range(n):
    D.append(int(input()))

print(sum(D))
print(max(0,2*max(D)-sum(D)))