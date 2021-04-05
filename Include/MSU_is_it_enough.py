s = "x@?,ea#OE{9%?L/OPL0OEL*LIL72I{2%6~2!If42f{2;"
key=""
key+=chr(ord(s[0])-ord('C'))
key+=chr(ord(s[1])-ord('S')+94)
key+=chr(ord(s[2])-ord('{')+94)
key+=chr(ord(s[len(s)-1])-ord('}')+188)
ans=""
ans+="CS{"
for i in range(3,len(s)-1):
    r = ord(s[i])-ord(key[i%4])
    while r < 33:
        r = r+94
    while r>=126:
        r = r-94
    ans+=chr(r)
print(ans+'}')