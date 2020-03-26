S = list(input())

ans = ['']*11
index = 0
for s in S:
    if s != 'B':
        ans[index] = s
        index += 1
    elif index >= 1:
        index -= 1
        ans[index] = ''
print(''.join(ans))
