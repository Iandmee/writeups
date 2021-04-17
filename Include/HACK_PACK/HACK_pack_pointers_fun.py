for i in range(1,200):
    for j in range(1,200):
        for u in range(1,200):
            for k in range(1,200):
                if ((k)|(u))&((j)|(i))==73 and len(chr(u).encode())==1 and len(chr(i).encode())==1 and len(chr(j).encode())==1 and len(chr(k).encode())==1:
                    print(chr(k).encode()+chr(u).encode()+chr(i).encode()+chr(j).encode())
                    exit(0)