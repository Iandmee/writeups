import base64
encoded = "xakgK\\Ns><m:i1>1991:nkjl<ii1j0n=mm09;<i:u"
key  = ""
xor = b"\x08"
for i in encoded:
	key+=chr(ord(i)^ord(xor))
print(key)