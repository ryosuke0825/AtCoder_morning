H, W = map(int, input().split())

S = []
for _ in range(H):
    hw = list(input())
    S.append(hw)

for i in range(H):
    for j in range(W):

        if S[i][j] == '.':
            continue

        # 上
        if i != 0 and S[i-1][j] == '#':
            continue
        # 下
        elif i != H-1 and S[i+1][j] == '#':
            continue
        # 左
        elif j != 0 and S[i][j-1] == '#':
            continue
        # 右
        elif j != W-1 and S[i][j+1] == '#':
            continue

        print('No')
        exit(0)
print('Yes')
