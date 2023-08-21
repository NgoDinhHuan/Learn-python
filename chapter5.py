def kiem_tra(chuoi):
    if len(chuoi) %2 !=0:
        return "ko doi xung"
    else:
        d=""
        c=""
        t = len(chuoi)//2

        for i in range(0,t):
            d=d + chuoi[i]
        for i in range(t, len(chuoi)):
            c = c + chuoi[i]
        return d,c
d,c = kiem_tra("abba")
print(d,c)