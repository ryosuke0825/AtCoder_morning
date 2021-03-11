S = input()

INF = 1000
i = INF
c = INF
t = INF

if S.find('i') != -1:
    i = S.find('i')
if S.find('I') != -1:
    i = min(S.find('I'), i)
if i == INF:
    print('NO')
    exit(0)

if S.find('c', i, len(S)) != -1:
    c = S.find('c', i, len(S))
if S.find('C', i, len(S)) != -1:
    c = min(S.find('C', i, len(S)), c)
if c == INF:
    print('NO')
    exit(0)


if S.find('t', c, len(S)) != -1:
    t = S.find('t', c, len(S))
if S.find('T', c, len(S)) != -1:
    t = min(S.find('T', c, len(S)), t)
if t == INF:
    print('NO')
    exit(0)


print('YES')
