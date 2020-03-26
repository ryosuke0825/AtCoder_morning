s = list(input())

ans = ''
char = s[0]
cnt = 1
for i in range(1, len(s)):
    if s[i] == char:
        cnt += 1
    else:
        ans += char+str(cnt)
        cnt = 1
        char = s[i]
ans += char+str(cnt)
print(ans)
