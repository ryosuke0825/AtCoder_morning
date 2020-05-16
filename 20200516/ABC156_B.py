import sys
sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline()[:-1]


N, K = map(int, input().split())
A = [0]*N
for _ in range(K):
    d = int(input())
    tmp = list(map(int, input().split()))
    for a in tmp:
        A[a-1] += 1

print(A.count(0))
