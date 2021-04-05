f = open("crypto.asm","rb")
TRX = b"GED\x03hG\x15&Ka =;\x0c\x1a31o*5M"
DRX = b""
lines = f.readlines()
for i in lines:
    start = i.strip().split()
    if start[0] == b"MOV":
        if start[1] == b"TRX":
            if start[2] == b'DRX':
                TRX = DRX
            else:
                TRX = start[2].replace(b"\"",b"")
        if start[1] == b"DRX":
            if start[2] == b'TRX':
                DRX = TRX
            else:
                DRX = start[2].replace(b"\"",b"")
    if start[0] == b'REVERSE':
        if start[1] == b"DRX":
            DRX = DRX[::-1]
        if start[1] == b"TRX":
            TRX = TRX[::-1]
    if start[0] == b"XOR":
        if start[1] == start[2]:
            if start[1] == b"TRX":
                TRX = b"\x00"
            else:
                DRX = b"\x00"
        else:
            temp = b""
            for i in range(min(len(TRX), len(DRX))):
                temp += chr(ord(chr(TRX[i])) ^ ord(chr(DRX[i]))).encode()
            if len(TRX) > len(DRX):
                temp += TRX[len(DRX):]
            elif len(TRX) != len(DRX):
                temp += DRX[len(TRX):]
            if start[1] == b"TRX":
                TRX = temp
            else:
                DRX = temp
print(TRX)
