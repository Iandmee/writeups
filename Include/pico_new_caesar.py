import string
cipher="apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"
alp = string.ascii_lowercase[:16]
for key in alp:
    temp=""
    for i in cipher:
        temp += alp[(ord(i)-ord(key)+ord('a')+len(alp))%len(alp)]
    ans=""
    for i in range(0,len(temp),2):
        k1 = alp.find(temp[i])
        k2 = alp.find(temp[i+1])
        k1*=16
        k1+=k2
        ans+=chr(k1)
    print(ans)