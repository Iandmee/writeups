x ='ADDEFECA'
x = int(x,16)
s = '464c41477b3132335245414c464c41472121217d'
for i in range(len(s)//8):
	x^=int(s[i*8:(i+1)*8],16)
temp = str(hex(x))[2:]
print(temp)
flag = 'e3c7ed8fdedfe481f6d4e59bfac6f597EECEF5B5'
ans = ''
for i in range(len(flag)//8):
	ans+=str(hex(int(temp,16)^int(flag[i*8:(i+1)*8],16)))[2:]
print(ans)