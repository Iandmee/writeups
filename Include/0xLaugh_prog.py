import hashlib
import string
s = "bd737ce0d884c0dd54adf35fdb794b60"
salt = "mmal7"
abc = string.ascii_lowercase+string.digits;
def decode1(d:str,n:int)->None:
    if(len(d)>n-1):
        return
    for j in abc:
        print(d+j)
        check = str(hashlib.md5((d+j+salt).encode()).hexdigest())
        if check == s:
            print("######################")
            print(1)
            print(d+j)
            print("#####################")
            exit(0)
        decode1(d+j,n)
def decode2(d:str,n:int)->None:
    if (len(d) > n-1):
        return
    for j in abc:
        check = str(hashlib.md5((salt+d+j).encode()).hexdigest())
        print(d+j)
        if check == s:
            print("######################")
            print(2)
            print(d + j)
            print("#####################")
            exit(0)
        decode1(d + j, n)
for i in range(1,7):
    for j in abc:
        decode1(j,5)
        decode2(j,5)

