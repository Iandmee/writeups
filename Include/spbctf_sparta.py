s = "st_3phr_b13gcsvut_3yf1rz{55}"
flag =[]
for i in range(len(s)):
    flag.append('a')
tec = 0
for i in range(7):
    for j in range(i,len(s),7):
        flag[j]=s[tec]
        tec+=1
for i in flag:
    print(i,end="")