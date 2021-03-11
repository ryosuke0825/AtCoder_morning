n, m = map(int, input().split())

# 短針を扱いやすいようにする12時間表記にする
if n >= 12:
    n -= 12

n_angle = n*30+(m*0.5)
m_angle = m*6

ans = min(max(n_angle, m_angle)-min(n_angle, m_angle), 360-(max(n_angle, m_angle)-min(n_angle, m_angle)))
print(ans)
