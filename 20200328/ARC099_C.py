import math

n, k = map(int, input().split())
A = list(map(int, input().split()))

print(math.ceil((n-k)/(k-1)+1))
