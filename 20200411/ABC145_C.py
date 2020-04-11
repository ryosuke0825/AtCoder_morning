import math

N = int(input())
XY = []
for _ in range(N):
    xy = list(map(int, input().split()))
    XY.append(xy)

ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        ans += math.sqrt(((XY[i][0]-XY[j][0])**2)+((XY[i][1]-XY[j][1])**2))

print(ans/N)
