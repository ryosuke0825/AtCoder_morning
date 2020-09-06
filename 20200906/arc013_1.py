NML = list(map(int, input().split()))
PQR = list(map(int, input().split()))

NML.sort()
PQR.sort()

if not(NML[0] >= PQR[0] and NML[1] >= PQR[1] and NML[2] >= PQR[2]):
    print(0)
else:
    ans1 = (NML[0]//PQR[0])*(NML[1]//PQR[1])*(NML[2]//PQR[2])
    ans2 = (NML[0]//PQR[0])*(NML[1]//PQR[2])*(NML[2]//PQR[1])
    ans3 = (NML[0]//PQR[1])*(NML[1]//PQR[2])*(NML[2]//PQR[0])
    ans4 = (NML[0]//PQR[1])*(NML[1]//PQR[0])*(NML[2]//PQR[2])
    ans5 = (NML[0]//PQR[2])*(NML[1]//PQR[0])*(NML[2]//PQR[1])
    ans6 = (NML[0]//PQR[2])*(NML[1]//PQR[1])*(NML[2]//PQR[2])
    print(max(ans1, ans2, ans3, ans4, ans5, ans6))
