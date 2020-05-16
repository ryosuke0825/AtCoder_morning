import math

N, K = map(int, input().split())
_ = list(map(int, input().split()))

ans = math.ceil((N-K)/(K-1)+1)
print(ans)
