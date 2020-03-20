def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


n = int(input())
divisors = make_divisors(n)

ans = 10**12
if len(divisors) % 2 == 0:
    for i in range(0, len(divisors), 2):
        ans = min(ans, divisors[i]+divisors[i+1])

else:
    for i in range(0, len(divisors)-1, 2):
        ans = min(ans, divisors[i]+divisors[i+1])
    ans = min(ans, divisors[-1]*2)
print(ans-2)
