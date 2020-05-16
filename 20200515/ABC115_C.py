import sys
sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline()[:-1]


N, K = map(int, input().split())
H = [0]*N
for i in range(N):
    H[i] = int(input())

H.sort()
ans = 10**10
for i in range(N-(K-1)):
    ans = min(ans, H[i+(K-1)]-H[i])
print(ans)
