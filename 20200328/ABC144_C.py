import math


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


n = int(input())
divisors = make_divisors(n)

ans = 10**13
for i in range(math.ceil(len(divisors)/2)):
    #print(divisors[i], divisors[len(divisors)-i-1])
    #print(divisors[i]+divisors[len(divisors)-i-1])
    ans = min(ans, divisors[i]+divisors[len(divisors)-i-1]-2)
print(ans)
