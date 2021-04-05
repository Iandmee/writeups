import base64
f = open("3","rb")
x = f.read()
needed = b"cd /secret_data;grep -R CS{;ech"
a = bytearray(x)
for i in range(len(needed)):
    a[i] = a[i] ^ needed[i]
a.append(ord(';'))
ans = bytes(a)
encoded_ans =  base64.b64encode(ans)
print(encoded_ans)