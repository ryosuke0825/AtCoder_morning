H, W, A, B = map(int, input().split())

for h in range(1, H+1):
    if h <= B:
        print('0'*A + '1'*(W-A))
    else:
        print('1'*A + '0'*(W-A))
